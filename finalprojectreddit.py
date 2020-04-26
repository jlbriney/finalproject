
#! usr/bin/env python3
import praw
import pandas as pan
import datetime as date
import nltk
import csv

# praw = Python Reddit API Wrapper
# connecting to Reddit API and storing it in variable "reddit"
reddit = praw.Reddit(client_id = 'sz9lkUOiWQCvSA', \
                     client_secret = 'cOd4rmjq5kM5QrGaDuTP4x0psgQ', \
                     user_agent='Matt Powers', \
                     username='206student', \
                     password='206student123')

# accessing the subreddit "Coronavirus"
subreddit = reddit.subreddit('Coronavirus')

# accessing the most up voted topics within the subbreddit "Coronavirus"
# limiting to only get 100 of the top topics
recent = subreddit.top(limit = 100)
headlines = []
for line in recent:
    date_post = line.created
    date_clean = date.datetime.fromtimestamp(date_post)
    line_tup = line.title, date_clean
    headlines.append(line_tup)


# nltk = Natural Language Toolkit used for working with human language data
# vader is used as a tool for sentiment analysis in social media
# importing the sentiment analysis class to use on top 100 topics
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


# creating instance of the class "SentimentIntensityAnalyzer"
sia = SIA()
results = []


# appending the polarity scores and their timestamps into a new list
for line in headlines:
    polarity_score = sia.polarity_scores(line[0])
    polarity_score['date'] = line[1]
    results.append(polarity_score)


# creating csv of each topic's polarity score
with open("reddit_sentiment_analysis.csv", "w", newline = "") as output:
    fileOut = csv.writer(output)
    data = [["Positive Score", "Negative Score", "Date"]]

    # writing header
    fileOut.writerows(data)

    # setting each value for csv
    for headline in results:
        positive_score = headline["pos"]
        negative_score = headline["neg"]
        date_post = headline["date"]

        # writing each line and values of csv
        fileOut.writerow([positive_score, negative_score, date_post])




