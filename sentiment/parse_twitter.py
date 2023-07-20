import datetime

def parse_twitts(start:datetime, end:datetime):
    # parse twitts from date {from} till date {to}
    # return twitts
    pass

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


if __name__ == "__main__":
    print('hello world')
    parse_twitts('01-01-2023', '01-02-2023')
    test_parse_twitts()
