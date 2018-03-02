"""
github.com/bschro99
"""


#Import libraries
import random
import tweepy
from time import sleep


#Import twitter credentials from credentials.py
from credentials import *


#Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Read the messages that we wrote in our messages.txt file
my_file = open('messages.txt', 'r')
file_lines = my_file.readlines()
my_file.close()


#Creating the function that will tweet a given line or our text file (i)
# with a given username (username)
def tweet(username,i):
        textline = file_lines[i]
        try:
                if textline != "\n":
                        line = ("@"+username+" ") + textline
                        if len(line)>140:
                                print("Too long")
                        else:
                                print(line)
                else:
                        pass
        except tweepy.TweepError as e:
                print(e.reason)
                sleep(2)


#Creating the function that will find the username of someone who's been tweeting
#with certain hashtags
def find_tweet(hashtag):
        for tweet in tweepy.Cursor(api.search, q=hashtag).items(10):
                try:
                        return tweet.user.screen_name
                except tweepy.TweepError as e:
                        print(e.reason)
                
                except StopIteration:
                        break


#The list of hashtags from  which our bot will pick one
hashtags = ["#depressed","#suicide","#sad","#suicidal","#anxiety","depression","#stress","#bipolar","#failure","#death"] #10 values in list



while True:
        hashtag_picked = random.randint(0,9)
        line_number = random.randint(0,32)      
        name = find_tweet(hashtag_picked)
        tweet(name,line_number)
        sleep(1000)

