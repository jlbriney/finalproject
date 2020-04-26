import os
import csv
import matplotlib
import matplotlib.pyplot as plt

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

corona_info = csv_reader("reddit_sentiment_analysis.csv")


def get_positive(info):
    positive_scores = []
    for line in info:
        line = line.split(",")
        positive_scores.append(line[0])
    return positive_scores

positive_scores = get_positive(corona_info)


def get_negative(info):
    negative_scores = []
    for line in info:
        line = line.split(",")
        negative_scores.append(line[1])
    return negative_scores

negative_scores = get_negative(corona_info)

# putting negative and positive scores of each headline in a tuple together
scores = list(zip(positive_scores, negative_scores))

positive = 0.0
negative = 0.0
neutral = 0.0

for score in scores:
    pos = score[0]
    neg = score[1]
    if pos > neg:
        positive += 1.0
    elif neg > pos:
        negative += 1.0
    else:
        neutral += 1.0

labels = ["Positive", "Negative", "Neutral"]
feelings = [positive, negative, neutral]
colors = ["lawngreen", "tomato", "yellow"]
explode = (0, 0, 0)

# creating pie chart
plt.pie(feelings, explode = explode, labels = labels, colors = colors, autopct = "%1.1f%%", shadow = True, startangle = 140)
plt.axis("Equal")
plt.title("Pie Chart of The Sentiments of the Top 100 Headlines Within the Subreddit of 'Coronavirus'")
plt.show()


# creating bar graph
plt.bar(labels, feelings)
plt.xlabel("Feelings")
plt.ylabel("Values")
plt.title("Bar Graph of The Sentiments of the Top 100 Headlines Within the Subreddit of 'Coronavirus'")
plt.grid(True)
plt.show()



