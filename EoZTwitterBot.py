# EoZ TwitterBot
#   Programmed by: ZenOokami
#   Http://EssenceOfZen.org ||
#
"""
A Twitter Bot written in Python utilizing Tweepy
The general design is to eventually have threads running in the background.
"""

import os
import csv
import tweepy
from time import gmtime, strftime
import time
from EoZAIkeys import *
import LogSnoot

# Notes =====================
# How searching can work
#
# We could have multiple search functions based off of parent functions
# One of these mechanics can be "FavTweet" "FollowUser" etc. -- depending on this function, we can run the proper
# search function and when the array is returned, we'll execute the action accordingly
#
# The function in question should check its results item with checked items,
# If the no match is found, run fine - and add the tweet to the checked list after.
#
# At the start of the process, we should always check the current date, then run the function that manages/clean the
# stored data for checked tweets.
#
#   Set up a CSV sheet for followers, following, and
# ============================


# Global Variables ==========
version = "v00.01.00"
todays_date = 0
processes_ran = 0
up_time = 0

search_tag_flag = 1
search_mention_flag = 1

checked_mention_tweets = []
checked_result_tweets = []
checked_authors = []


# ===========================

# Threads ===================
# We should have a thread for every automatic functionality we have:

def searchingMentionsThread(): # Search For Mentions every x amount of time
    global search_mention_flag
    global checked_tweets

    while(True):
        while(search_mention_flag):
            time.sleep(60 * 30)  # sleep for 30 minutes
            pass


def searchingEoZTagThread(): # Search for #EoZ tags and possibly others
    global checked_result_tweets

    while(True):
        while(search_tag_flag):
            time.sleep(60 * 60)  # sleep for 30 minutes
            pass


# def something

# ===========================

# Functions =================
def authenticate():  # Authenticate the Connection
    authentication = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    authentication.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = tweepy.API(authentication)
    return tweepy.API(authentication)


def SendTweet(tweet):
    # Authenticate the connection
    # authentication = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # authentication.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # twitter_api = tweepy.API(authentication)

    # Sending the tweet
    try:
        twitter_api.update_status(tweet)
        LOG.writeI("Attempting to update status with: " + tweet)
    except tweepy.TweepError as error:
        LOG.writeE(error)
        LOG.space()
    else:
        LOG.writeI("System Tweeted: " + tweet)
        LOG.space()

    print("")


def search(input): # A genuine search function
    try:
        results = twitter_api.search(input)
    except tweepy.TweepError as error:
        print(error)
    else:
        return results


def setTodaysDate():
    global todays_date
    today_year = time.strftime("%Y")
    today_month = time.strftime("%m")
    today_day = time.strftime("%d")
    todays_date = [today_year, today_month, today_day]


def getTodaysDate():
    global todays_date
    return todays_date


def checkDates(current_day, previous_date):
    # Current day will be an array: [0]=year, [1]=month, [2]=day
    # Check year
    if (int(current_day[0] > previous_date.year)):
        # A new year
        # if statement
        pass
    else:
        # Same year, check for month
        if (int(current_day[1]) > previous_date.month):
            # a new month
            # if statement
            pass
        else:
            # Same month, check day
            if (int(current_day[2]) > previous_date.day):
                # a new day
                pass
            else:
                # same day, either check ID or check
                pass


def followUser(tweet):
    tweet.author.follow();


def favoriteTweet(tweet):
    tweet.favorite()


def retweetTweet(tweet):
    tweet.retweet();


def compareTweetID(index, id):  # Allows us to see if a current id is equal to a list of previously checked
    global checked_tweets
    # We can return a bool that allows us to check if the item has been checked already.
    if (checked_tweets[index] == id):
        return True
    else:
        return False


def compareAuthorID(index, id):  #
    global checked_authors
    if (checked_authors[index] == id):
        return True
    else:
        return False


# Search functions should contain a system of dates to check and compare to see if the results have already been seen
def searchForTags(tag):  # returns an array
    try:
        results = twitter_api.search('#' + tag)
        LOG.writeI("Searching for Hashtag: " + tag)
    except tweepy.TweepError as error:
        print(error)
        LOG.writeE(error)
        LOG.space()
    else:
        LOG.writeI("Search Completed, for: " + tag)
        LOG.space()
        return results


def searchForUser(user):
    try:
        user_list = twitter_api.search_users(user)
        print("Searching for user: " + user)
        LOG.writeI("Searching for the user: ")
    except tweepy.TweepError as error:
        print(error)
        LOG.writeE(error)
        LOG.space()
    else:
        LOG.writeI("Search Completed for, " + user)
        LOG.space()
        return user_list


def searchForMentions(mention):
    try:
        pass
    except tweepy.TweepError as error:
        pass
    else:
        pass


def menu():
    # Tweet, search for hashtag, grab latest tweet from user, run a custom protocol
    # print("|" + "|".rjust(20,'='))
    print("|".ljust(44,"=") + "|")
    print("|- Tweet [t]".ljust(44) + "|")
    print("|- Search Hashtag [sh]".ljust(44)+"|")
    print("|- Latest Tweet From User [lt]".ljust(44) + "|")
    print("|- Run Custom Protocol [rcp]".ljust(44) + "|")
    print("|".ljust(44) + "|")
    print("|- Exit [e]".ljust(44) + "|")
    print("|".ljust(44,"=")+"|")
    print("|- EoZTweetBot " + version.ljust(29) + "|")
    print("|".ljust(44,"=")+"|")


def main():
    system = 1
    while system == 1:
        menu()
        # Get user input
        user_input = input("Command: ")
        # Check the command
        if (user_input.lower() == "tweet") or (user_input.lower() == "t"):
            user_input = input("Please input tweet: ")
            SendTweet(user_input)
            print("")
        elif (user_input.lower() == "search hashtag"):
            pass
        elif (user_input.lower() == "latest tweet from user"):
            pass
        elif (user_input.lower() == "Run Custom Protocol"):
            pass
        elif (user_input.lower() == "exit"):
            # Turn off the loop
            system = 0
        else:
            print("Invalid input")

    # System off
    LOG.close()  # stop our snooper
    print("Shutting down AI unit...")


# ======================================
LOG = LogSnoot.Snoop()  # Start our snooper
twitter_api = authenticate()  # Set our API

main()  # Main function runs our main function for user input
