import tweepy
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt
import sqlite3
import os
import requests
import io
import pandas as pd


# credentials from https://apps.twitter.com/
consumer_key = 'w4ZEDgu44FuF3JAX4E37H5Gfz'
consumer_secret = 'dVGOh2I0VOVUoo9niL3sUF4nintXmfqdFmDfQsfA5P9BvOsW7F'
access_token = '2918269245-4z9nPDSc0WWuiHs1rHmd6fgMvTQCw1bwHGuNG8J'
access_token_secret = 'Gj1J0X6bPBui1ZD1ZU56gRMMXdXYZUsUELtPx4JqDhcFH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#function for getting a list of tweets from a user, making sure relvant hashtag is in tweet

def list_tweets(user_id, count, prt=False):
    tweets = api.user_timeline("@" + user_id, count=count, tweet_mode='extended')
    tweets_list = []

    for t in tweets:
            if "#COVID19" in t.full_text and len(tweets_list) < 100:
                tweets_list.append(t.full_text)
                if prt:
                    print(t.full_text)
                    print()
    return tweets_list


user_id = 'WHO'
count=200

tweets_list_who = list_tweets(user_id, count)
polarity_list = []
subjectivity_list = []
overall_list = []

#counts for sentiment analysis
pos = 0
neg = 0
neu = 0

print(tweets_list_who)

with open('twitter_sentiment_analysis.csv', 'w', newline = '') as output:

    # create var
    fileOut = csv.writer(output)
    data = [['Tweets', 'Polarity', 'Subjectivity', 'overall']]

    fileOut.writerows(data)

    for tweet in tweets_list_who:
        analysis = TextBlob(tweet)
        polarity = analysis.sentiment.polarity
        polarity_list.append(polarity)
        subjectivity = analysis.sentiment.subjectivity
        subjectivity_list.append(subjectivity)
        if analysis.sentiment.polarity > 0: 
            overall = 'positive'
            pos += 1
            overall_list.append(overall)
        elif analysis.sentiment.polarity == 0: 
            overall =  'neutral'
            neu += 1
            overall_list.append(overall)
        else: 
            overall = 'negative'
            neg += 1
            overall_list.append(overall)

                
        fileOut.writerow([tweet, polarity, subjectivity, overall])

        #uncomment below if you want to print these to the terminal
        
        #print (tweet)
        #print ('Polarity: ', polarity)
        #print ('Subjectivity:', subjectivity)
        #print ('Overall:', overall)


def open_db():
    conn = sqlite3.connect('/Users/haileyquinn/Desktop/WHOtwitter.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS WHOTwtterSentiments')
    cur.execute("CREATE TABLE IF NOT EXISTS WHOTwitterSentiments(tweet TEXT, polarity INTEGER, subjectivity INTEGER, overall TEXT)") 
    
#create database table from csv file info
def write_db(tweets, polarities, subjectivities, overalls): 
    try:
        conn = sqlite3.connect('/Users/haileyquinn/Desktop/WHOtwitter.db')
        cur = conn.cursor()
        for x in range(20):
            tweet = tweets[x]
            polarity = polarities[x]
            subjectivity = subjectivities[x]
            overall = overalls[x]
            cur.execute("INSERT INTO WHOTwitterSentiments (tweet, polarity, subjectivity, overall) VALUES (?,?,?,?)", (tweet, polarity, subjectivity, overall))
            conn.commit()
        print('Success')
        cur.close()
    except:
        print("Data inputed in table but not enough data for 20 new rows")

#limiting to 20 uploads at a time
open_db()
write_db(tweets_list_who, polarity_list, subjectivity_list, overall_list)
write_db(tweets_list_who[20:], polarity_list[20:], subjectivity_list[20:], overall_list[20:])
write_db(tweets_list_who[40:], polarity_list[40:], subjectivity_list[40:], overall_list[40:])
write_db(tweets_list_who[60:], polarity_list[60:], subjectivity_list[60:], overall_list[60:])
write_db(tweets_list_who[80:], polarity_list[80:], subjectivity_list[80:], overall_list[80:])

#making a pie chart of the sentiments!
labels = 'Positive', 'Negative', 'Neutral'
sizes = [pos , neg , neu]
colors = ['lightskyblue', 'lightcoral', 'lemonchiffon']
explode = (0, 0, 0)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title("The Sentiments of @WHO about COVID-19 on Twitter")
plt.show()

#to finish running the program, must close pop up pie chart