import sys
import tweepy
import os
import pprint
import datetime
import csv

# ---------------------------------------------
# --------------VARIABLES----------------------
# ---------------------------------------------

# TWITTER VARIABLES
consumer_key = 'DDrwYJLIgDvm7WOi0up9wmdNG'
consumer_secret = '5VDCEj3dnnxyuirn0sHYR0ULyjDdgApAocAX71C53flJwHlmel'
access_token = '3339394299-U3AB1hJBHTiuImeyhhoDkEBFDjL2bopSVk425yp'
access_token_secret = 'j5FMNfZ73Tub0zln1eZg8we92TiXgfZUi0fDshklxaZsK'

# Persistent Variables
herolist = {}
nerfedherolist = {}

# TWITTER AUTHENTICATION SETUP
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ---------------------------------------------
# --------------Reading in---------------------
# ---------------------------------------------

reader = csv.reader(open('herolist.csv', 'r'))
for row in reader:
   k, v = row
   herolist[k] = v

# Converting all the numbers that were strings to ints
for hero in herolist:
    herolist[hero] = int(herolist[hero])

reader = csv.reader(open('nerflist.csv', 'r'))
for row in reader:
    k, v = row
    nerfedherolist[k] = v
# Converting all the numbers that were strings to ints
for hero in nerfedherolist:
    nerfedherolist[hero] = int(nerfedherolist[hero])

# ---------------------------------------------
# ---------------Actual Code-------------------
# ---------------------------------------------

# Getting the date in a format that can be used in the TweePy lib
i = datetime.datetime.now()
# formats it
currdate=("%s" % i)
# Gets only the relevant date and removes any trailing characters.
currdate=currdate[:10]


# checking the '#Overwatch' to see what people mention
for tweet in tweepy.Cursor(api.search, q='#overwatch', since=currdate ).items(300):
    #looping around to see if they mention an overwatch hero in their tweet.
    for hero in herolist:
        if(hero in tweet.text):
            print(hero + "  Is mentioned below: ")
            print(tweet.text)
            herolist[hero]=herolist[hero]+1
            print("------------------")

print(herolist)


"""

print(herolist['Ana'])
herolist['Ana']=herolist['Ana']+1
print(herolist['Ana'])


"""
