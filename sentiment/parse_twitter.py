import datetime
import os, re, sys, time, random
import undetected_chromedriver
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def parse_twitts(start:datetime, end:datetime):
    # parse twitts from date {from} till date {to}
    # return twitts
    # Add the Chrome options path to the environment variable
    os.environ['PATH'] += r"/chrome-linux64/"

    # Define the Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=/home/i2p/Documents/pars/chrome-linux64/Profile 2')

    # Initialize the Chrome WebDriver
    driver = undetected_chromedriver.Chrome(options=chrome_options)

    # Database connection settings
    db_connection = sqlite3.connect('twitter_scraper.db')
    cursor = db_connection.cursor()

    # Create a table to store the scraped data
    cursor.execute('''CREATE TABLE if not exists twitter_results
                     (id INTEGER PRIMARY KEY, title TEXT, description TEXT)''')

    # Your test code here

    url = "https://twitter.com/home"  # Replace with the webpage you want to test

    # Launch the browser and switch to the default content
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Wait for the tweet text element to be present
    tweet_text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetText']"))
    )
    elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='cellInnerDiv']")[0]

    #Search for the first message to be parsed to in the next iteration
    first_message = elements.find_element(By.CSS_SELECTOR, "[data-testid='tweetText']").text
    nick_name = re.findall(r'@\S+', elements.text)
    parsing_to_this_message_1 = " İyi Geceler #Galatasaray Ailesi  @GalatasaraySK"
    parsing_to_this_message_2 = first_message + " " + str(nick_name[0])

    #How deep to parse to
    deep_to_parse = 50

    #print(parsing_to_this_message)

    scraped_titles = set()
    i = 0

    time.sleep(5)  # Wait for the page to load
    while True:
        try:
            # Random scroll down the page       
            scroll_speed = random.uniform(0.9, 1.8)  # Generate a random scroll speed between 0.5 and 2 seconds
            current_position = driver.execute_script("return window.pageYOffset;")
            random_pix = random.uniform(3000, 4000)
            target_position = current_position + random_pix
            driver.execute_script(f"window.scrollTo(0, {target_position});")
            time.sleep(scroll_speed)

            # Wait for the tweet text element to be present
            tweet_text_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetText']"))
            )
            # Scrape the elements
            elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='cellInnerDiv']")
            i += 1
            print("Ok: " + str(i))
            done_inner_loop = False

            # Write the scraped data to the SQLite database without duplicates
            for element in elements:
                if done_inner_loop == True:
                    print("done_inner_loop = True")
                    break

                title = element.find_element(By.CSS_SELECTOR, "[data-testid='tweetText']").text
                description = element.find_element(By.CSS_SELECTOR, "time[datetime]").text
                nick_name = re.findall(r'@\S+', element.text)
                parsing_to_this_message_maybe = title + " " + str(nick_name[0])

                print((len(scraped_titles)))
    #            print(parsing_to_this_message_1)
    #            print(parsing_to_this_message_2)
                print(parsing_to_this_message_maybe)
                # Check if the title is already in the set
                if title not in scraped_titles:
                    # Parses to the depth defined in the variable "deep_to_parse" or to the first message in the previous iteration.
                    if len(scraped_titles) > deep_to_parse or parsing_to_this_message_1 == parsing_to_this_message_maybe:
                        # Refresh the page and continue parsing
                        driver.execute_script("window.location.reload();")
                        scraped_titles = set()
                        done_inner_loop = True
                        parsing_to_this_message_1 = parsing_to_this_message_2
                        # Wait for the tweet text element to be present
                        tweet_text_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetText']"))
                        )
                        elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='cellInnerDiv']")[0]

                        #Search for the first message to be parsed to in the next iteration
                        first_message = elements.find_element(By.CSS_SELECTOR, "[data-testid='tweetText']").text
                        nick_name = re.findall(r'@\S+', elements.text)
                        parsing_to_this_message_2 = first_message + " " + str(nick_name[0])
                        print("Found the tweeter to parse to")
                        time.sleep(8)
                        break

                    scraped_titles.add(title)
                    cursor.execute("INSERT INTO twitter_results (title, description) VALUES (?, ?)", (title, description))
                    db_connection.commit()

            print(len(scraped_titles))
        # Handle NoSuchElementException error
        except Exception as e:
            if "NoSuchElementException" in str(e):
                print("Error: No such element found. Pausing for 3 seconds before continuing...")
                time.sleep(3)
                continue  # Resume the loop
            else:
                print(e)  # Print the error message for other exceptions
    #           break  # Exit the loop if another exception occurs
    #            print("Error: ...")
                time.sleep(3)
                continue  # Resume the loop
    #Close the browser when finished
    time.sleep(1)

    driver.quit()
    db_connection.close()

def test_parse_twitts():
    # test parse twitts functionality somehow
    # For example:
    start = '01-01-2022'
    end = '01-02-2022'
    result = parse_twitts('01-01-2023', '01-02-2023')

    assert result is not None
    print('done. result is good')
    # check result object here
    # we can check that some object properties
    # like time of twitt creation are correct
    for twitt in result:
        assert twitt['date'] > start and twitt['date'] <= end


def test_selenium():
    # driver = webdriver.Chrome('/the directory where the web driver')
    # driver = webdriver.Chrome('/chrome-linux64/chrome')
    print('dirs: ', os.listdir())
    driver = webdriver.Chrome('../chrome-linux64')
    driver.get('http://www.google.com')
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    # parse_twitts('01-01-2023', '01-02-2023')
    test_selenium()
    # test_parse_twitts()
