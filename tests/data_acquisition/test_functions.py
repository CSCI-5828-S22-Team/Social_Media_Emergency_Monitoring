import tweepy
import csv
import pickle
from datetime import datetime
from config import *
from test_functions import *

import requests
import unittest
from unittest import mock

def read_in_tweets(mock_tweets):
    if isinstance(mock_tweets, dict):
        print("\t* read_in_tweets\t-\tSUCCESS")
        return True

def check_length(mock_tweets):
    if len(mock_tweets) != 25:
        print("\t* check_length\t\t-\tFAIL")
        return False
    print("\t* check_length\t\t-\tSUCCESS")
    return True

def convert_to_dt(mock_tweets):
    type_holder = type(datetime.strptime('2022-04-14 13:03:52', '%Y-%m-%d %H:%M:%S'))
    for tweet in mock_tweets:
        mock_tweets[tweet]['created_at'] = datetime.strptime(str(mock_tweets[tweet]["created_at"]), '%Y-%m-%d %H:%M:%S')
    try:
        for tweet in mock_tweets:
            isinstance(mock_tweets[tweet]['created_at'],  type_holder) == True
    except:
        print("\t* convert_to_dt\t\t-\tFAIL")
        print("\t* datetime object failing, type is {0}".format(type(mock_tweets[tweet]['created_at'])))
        return False
    print("\t* convert_to_dt\t\t-\tSUCCESS")
    return True

def check_all_types(mock_tweets):
    count = -1
    type_holder = type(datetime.strptime('2022-04-14 13:03:52', '%Y-%m-%d %H:%M:%S'))
    for tweet in mock_tweets:
        count+=1
        if (isinstance(mock_tweets[tweet]['user_screen_name'],  str) == True) and \
            (isinstance(mock_tweets[tweet]['created_at'],  type_holder) == True) and \
            (isinstance(mock_tweets[tweet]['text'],  str) == True):
            continue
        else:
            print("\t* check_all_types\t-\tFAIL")
            return False
    print("\t* check_all_types\t-\tSUCCESS")
    return True

def check_tweet_size(mock_tweets):
    for tweet in mock_tweets:
        if len(mock_tweets[tweet]) != 3:
            print("\t* check_tweet_size\t-\tFAIL")
            return False
    print("\t* check_tweet_size\t-\tSUCCESS")
    return True

def check_tokens(access_token, access_token_secret, consumer_key, consumer_secret):
    args = []
    args.append(access_token)
    args.append(access_token_secret)
    args.append(consumer_key)
    args.append(consumer_secret)
    for arg in args:
        if not isinstance(arg,  str):
            print("\t* check_tokens\t\t-\tFAIL")
            return False
    print("\t* check_tokens\t\t-\tSUCCESS")
    return True

def get_tweets(access_token, access_token_secret, consumer_key, consumer_secret, filename = default_filename, locations = default_locations, search_words = default_words, tweet_count = 5000):
    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    auth_api = tweepy.API(auth, wait_on_rate_limit=True)

    search_count = (5000 if tweet_count > 10000 else tweet_count)
    count = 0
    tweets = tweepy.Cursor(auth_api.search_tweets, q=[default_locations[0], default_words[0]], lang="en").items(search_count)
    with open('mock_api.pickle', 'wb') as f:
        pickle.dump(tweets, f)
    print("Pickle file written ✅")

def mock_api(pickle_file):
    with open(pickle_file, "rb") as input_file:
        response = pickle.load(input_file)
    if isinstance(response, tweepy.cursor.ItemIterator) == True:
        print("\t* mock_api\t\t-\tSUCCESS")
        return True
    print("\t* mock_api\t\t-\tFAIL")
    return False
