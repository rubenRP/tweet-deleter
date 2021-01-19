# Tweet Deleter
Complete script made in Python that allows to delete all the tweets of an account given a date range. For this it makes use of the Twitter API so it is necessary to have a Twitter Developers account
## Configuration
1. Add the API keys in remove-tweets.py file:

```
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""
```

2. Modify the date range:

```
range_start = parse_datetime('Sep 10 00:00:00 +0000 2007')
range_end = parse_datetime('Jan 10 00:00:00 +0000 2019')
```

3. Run the script

```
python tweet-deleter.py
