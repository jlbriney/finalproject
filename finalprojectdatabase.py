import os
import csv
import sqlite3


# creating function to read csv and leaving out header of csv
def csv_reader(filename):
    root_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(root_path, filename)
    file_obj = open(filename, "r")
    file_data = file_obj.readlines()
    with open(filename) as file_obj:
        file_data = file_obj.readlines()
    for i in range(len(file_data)):
        file_data[i] = file_data[i].replace("\n", "")
    return file_data[1:]

# creating instance of the csv reader 
corona_info = csv_reader("reddit_sentiment_analysis.csv")


# gets only positive scores from csv
def get_positive(info):
    positive_scores = []
    for line in info:
        line = line.split(",")
        positive_scores.append(line[0])
    return positive_scores

positive_scores = get_positive(corona_info)

# gets only negative scores from csv
def get_negative(info):
    negative_scores = []
    for line in info:
        line = line.split(",")
        negative_scores.append(line[1])
    return negative_scores

negative_scores = get_negative(corona_info)


# gets only dates from csv
def get_date(info):
    dates = []
    for line in info:
        line = line.split(",")
        dates.append(line[2])
    return dates

dates = get_date(corona_info)



def open_db():
    conn = sqlite3.connect("/Users/mattpowers/Desktop/SI206/CoronavirusProject.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS RedditScores")
    cur.execute("CREATE TABLE IF NOT EXISTS RedditScores(Positivity FLOAT, Negativity FLOAT, Date TEXT)")


#creating a database table from a csv file
def write_db(positive_scores, negative_scores, dates):
    try:
        conn = sqlite3.connect("/Users/mattpowers/Desktop/SI206/CoronavirusProject.db")
        cur = conn.cursor()
        for i in range(20):
            pos_score = positive_scores[i]
            neg_score = negative_scores[i]
            date = dates[i]
            cur.execute("INSERT INTO RedditScores (Positivity, Negativity, Date) VALUES(?,?,?)", (pos_score, neg_score, date))
            conn.commit()
        print("Success")
        cur.close()
    except:
        print("Something went wrong with data.")


# writing into database with only 20 rows of data at a time
open_db()
write_db(positive_scores, negative_scores, dates)
write_db(positive_scores[20:], negative_scores[20:], dates[20:])
write_db(positive_scores[40:], negative_scores[40:], dates[40:])
write_db(positive_scores[60:], negative_scores[60:], dates[60:])
write_db(positive_scores[80:], negative_scores[80:], dates[80:])


