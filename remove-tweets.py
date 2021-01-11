# ==================================================================
# Import statements
# ==================================================================

import sys
import time
from datetime import datetime
import os
import twitter
from dateutil.parser import parse
import numpy as np
import pandas as pd
import json
from datetime_z import parse_datetime


# ==================================================================
# API Credentials
# ==================================================================

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""


# ==================================================================
# Initialize
# ==================================================================

api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN_KEY,
                  access_token_secret = ACCESS_TOKEN_SECRET)


# ======================================================================================
# Function to delete tweet by ID
# ======================================================================================

def deleteTweet(tweetId):
   try:
     print("Deleting tweet #{0})".format(tweetId))
     api.DestroyStatus(tweetId)
     print("Deleted")

   except Exception as err:
      print("Exception: %s\n" % err)


# ======================================================================================
# ======================================================================================

myData = None
with open('editedTweet.json') as json_file:
    myData = json.load(json_file)

# ======================================================================================
# Just printing one object to show the contents of tweet object
# ======================================================================================

myData["data"][0]


# ======================================================================================
# Select date range within which tweets will be deleted rememeber the UTC offset here
# ======================================================================================

range_start = parse_datetime('Sep 10 00:00:00 +0000 2007')
range_end = parse_datetime('Jan 10 00:00:00 +0000 2019')

# ======================================================================================
# I am creating a list of tweet IDs for consideration, where tweetsToBeDeleted will be
# used for deleting tweet
# ======================================================================================

tweetsToBeDeleted = []
tweetsToBeIgnored = []

for element in myData["data"]:
  tweet_post_time = parse_datetime(element["tweet"]["created_at"])
  if (tweet_post_time>= range_start and tweet_post_time<= range_end ):
    tweetsToBeDeleted.append(element["tweet"]["id_str"])
  else:
    tweetsToBeIgnored.append(element["tweet"]["id_str"])

print(len(tweetsToBeDeleted),len(tweetsToBeIgnored))


# ======================================================================================
# Now iterate over the list and pass each id to delete function, remember if you have
# over 1000+ tweets make sure to remove the print statement from delete function as it 
# will print id of each tweet while deleting
# ======================================================================================

for id in tweetsToBeDeleted:
  deleteTweet(id)
