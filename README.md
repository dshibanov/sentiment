# Parse twitter for text messages


### 0 Package installation, use the following commands:

        ```sudo apt update```

        ```sudo apt install -y python3```

        ```sudo apt install -y python3-pip```

        ```sudo apt install -y unzip```

        ```sudo apt install -y sqlite3```

        ```sudo pip3 install selenium==4.9```

        ```sudo pip3 install undetected_chromedriver==3.5.0```
     

### 1 Download and install Google Chrome

It is important that the version of google chrome and the version of the chromedriver must match (example: 117.0.5938.92 and 117.0.5938.92)!

Download either the latest versions of google chrome and webdrivers or google chrome and webdrivers version 117.0.5938.92.

Download google chrome

    The latest version of google chrome:

        ```https://www.google.com/chrome/index.html```

    Google Chrome 117.0.5938.92:

        ```https://www.sendspace.com/file/dlqvgx```
        
Install google chrome
        
        ```sudo apt install -f -y ./google-chrome-stable_current_amd64.deb```        


### 2 Download and install chromedriver 

It is important that the version of google chrome and the version of the webdriver must match (example: 117.0.5938.92 and 117.0.5938.92)!

Download either the latest versions of google chrome and webdrivers or google chrome and webdrivers version 117.0.5938.92.

Download chromedriver:

    The latest version chromedriver:
    
        ```https://googlechromelabs.github.io/chrome-for-testing/```
        
    Chromedriver version 117.0.5938.92:
    
        ```https://www.sendspace.com/file/r3irjl```
        
Install chromedriver:

        ```cd /sentiment```
        ```unzip chrome-linux64.zip```


### 3 Test and customize the browser for future work

        ```cd /sentiment```
        ```python3 parse_twitter.py```

If everything is installed correctly, the test script and the whoer.net site will start. 

1. check undetected_chromedriver plugin operation:

    whoer.net -> Extended version -> Navigator -> webdriver false

2. If you want to customize anti-detect browser, if they will ban the accounts, so that the next accounts are not banned need a new browser fingerprint.

Plugins for changing browser fingerprints:

    Trace - Online Tracking Protection
        ```https://chrome.google.com/webstore/detail/trace-online-tracking-pro/njkmjblmcfiobddjgebnoeldkjcplfjb?utm_source=ext_app_menu```
    User-Agent Switcher and Manager
        ```https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg?utm_source=ext_app_menu```
    Change Timezone (Time Shift)
        ```https://chrome.google.com/webstore/detail/change-timezone-time-shif/nbofeaabhknfdcpoddmfckpokmncimpj?utm_source=ext_app_menu```
    Font Fingerprint Defender
        ```https://chrome.google.com/webstore/detail/font-fingerprint-defender/fhkphphbadjkepgfljndicmgdlndmoke```
    AudioContext Fingerprint Defender
        ```https://chrome.google.com/webstore/detail/audiocontext-fingerprint/pcbjiidheaempljdefbdplebgdgpjcbe```

Check the work of plug-ins and browser fingerprint settings on 
        ```https://browserleaks.com/```

3. Go to https://twitter.com/ and log in. Go to the subscription feed. In test mode, all settings, cookies are saved.

4. edit file parse_twitter.py

        ```
        if __name__ == "__main__":
        parse_twitts('01-01-2023', '01-02-2023')
        #test_selenium()
        # test_parse_twitts()
        ```
    Run the script:
        ```python3 parse_twitter.py```

Result in file - twitter_scraper.db



