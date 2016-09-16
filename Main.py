import urllib, json
import sys
import tweepy
import os
import time
import datetime
from tweepy import OAuthHandler
import csv

# TWITTER VARIABLES

consumer_key = 'DDrwYJLIgDvm7WOi0up9wmdNG'
consumer_secret = '5VDCEj3dnnxyuirn0sHYR0ULyjDdgApAocAX71C53flJwHlmel'
access_token = '3339394299-U3AB1hJBHTiuImeyhhoDkEBFDjL2bopSVk425yp'
access_token_secret = 'j5FMNfZ73Tub0zln1eZg8we92TiXgfZUi0fDshklxaZsK'

# Persistent Variables
characterfrequency = {}
nerfedfrequency = {}

# TWITTER AUTHENTICATION SETUP
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Getting the date in a format that can be used in the TweePy lib
i = datetime.datetime.now()
# formats it
currdate=("%s" % i)
# Gets only the relevant date and removes any trailing characters.
currdate=currdate[:10]


# Doing a file + dictionary for seeing how frequently a character is mentioned.
reader = csv.reader(open('characterlist.csv'))
for row in reader:
    key = row[0]
    if key in characterfrequency:
        pass
    characterfrequency[key] = row[1:]
print(characterfrequency)

# checking the '#Overwatch' to see what people mention
for tweet in tweepy.Cursor(api.search, q='#overwatch', since=currdate ).items(100):
    #looping around to see if they mention an overwatch hero in their tweet.
    for hero in characterfrequency:
        if(hero in tweet.text):
            print(hero + "  Is mentioned below: ")
            print(tweet.text)
            print("------------------")
