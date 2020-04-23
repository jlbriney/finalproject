import csv
import sqlite3
import os
import requests
import io
import pandas as pd

#read into github website to get raw file
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
data = requests.get(url).content
#convert bytes to string format
corona_info = str(data, 'utf-8')

corona = corona_info.split(' ')




#write csv file from github data
with open('corona.csv', 'w', newline = '') as f:
    write = csv.writer(f)
    for info in corona:
        info = info.split('\n')
        for num in info:
            num = num.split(',')
            write.writerow([num[0], num[1], num[2]])

#read through csv file
def csv_reader(filename):
    root_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(root_path, filename)
    file_obj = open(filename, 'r')
    file_data = file_obj.readlines()
    with open(filename) as file_obj:
        file_data = file_obj.readlines()
    for i in range(len(file_data)):
        file_data[i] = file_data[i].replace('\n', '')
    return file_data[1:]

us_corona_info = csv_reader('corona.csv')

#read through csv file and return a list of all of the dates 
def get_date_data(info):
    dates = []
    for val in info:
        val = val.split(',')
        dates.append(val[0])
    return dates

#a list of all of the dates
date_info = get_date_data(us_corona_info)

#read through csv file and return a list of the # of cases
def get_cases_data(info):
    cases = []
    for val in info:
        val = val.split(',')
        cases.append(val[1])
    return cases

#a list of cases
no_of_cases = get_cases_data(us_corona_info)    

#read through csv file and return a list of # of deaths
def get_deaths_data(info):
    deaths = []
    for val in info:
        val = val.split(',')
        deaths.append(val[2])
    return deaths

#a list of death counts
no_of_deaths = get_deaths_data(us_corona_info)
    

def open_db():
    conn = sqlite3.connect('/Users/jordanbriney/Desktop/Coronavirus.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS USCases')
    cur.execute("CREATE TABLE IF NOT EXISTS USCases(date TEXT, cases INTEGER, deaths INTEGER)") 
    
#create database table from csv file info
def write_db(date_info, no_of_cases, no_of_deaths): 
    try:
        conn = sqlite3.connect('/Users/jordanbriney/Desktop/Coronavirus.db')
        cur = conn.cursor()
        for x in range(20):
            date = date_info[x]
            cases = no_of_cases[x]
            deaths = no_of_deaths[x]
            cur.execute("INSERT INTO USCases (date, cases, deaths) VALUES (?,?,?)", (date, cases, deaths))
            conn.commit()
        print('Success')
        cur.close()
    except:
        print("Data inputed in table but not enough data for 20 new rows")

#limiting to 20 uploads at a time
open_db()
write_db(get_date_data(us_corona_info), get_cases_data(us_corona_info), get_deaths_data(us_corona_info))
write_db(get_date_data(us_corona_info)[20:], get_cases_data(us_corona_info)[20:], get_deaths_data(us_corona_info)[20:])
write_db(get_date_data(us_corona_info)[40:], get_cases_data(us_corona_info)[40:], get_deaths_data(us_corona_info)[40:])
write_db(get_date_data(us_corona_info)[60:], get_cases_data(us_corona_info)[60:], get_deaths_data(us_corona_info)[60:])
write_db(get_date_data(us_corona_info)[80:], get_cases_data(us_corona_info)[80:], get_deaths_data(us_corona_info)[80:])


import matplotlib
import matplotlib.pyplot as plt

#read through corona.csv to make each column into a list
with open('corona.csv', 'r') as csv_file:
    csv_read = csv.reader(csv_file, delimiter = ',')
    date = []
    num_cases = []
    num_deaths = []
    for lines in csv_read:
        date.append(lines[0])
        num_cases.append(lines[1])
        num_deaths.append(lines[2])
    date_list = date[1:]
    cases_list = num_cases[1:]
    cases_list = [int(i) for i in cases_list]
    deaths_list = num_deaths[1:]
    deaths_list = [int(i) for i in deaths_list]
    
    y = date_list
    d1 = cases_list
    d2 = deaths_list

    fig, ax = plt.subplots()
    ax.plot(y, d1, 'b-', label = "Number of Cases")
    ax.plot(y, d2, 'g-', label = "Number of Deaths")
    ax.legend()
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of People')
    ax.set_title('COVID-19 in the USA')
    plt.xticks(rotation = 'vertical', fontsize = 4)
    ax.grid()
    # save the line graph
    fig.savefig("test.png")

    # show the line graph
    plt.show()

        
#calculation
def get_db_info():
    conn = sqlite3.connect('/Users/jordanbriney/Desktop/Coronavirus.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM USCases")
    result = cur.fetchall()
    return result

lst_uscases = get_db_info()

def make_cases_lst(lst1):
    cases = []
    for info in lst1:
        cases.append(info[1])
    return cases

cases1 = make_cases_lst(lst_uscases)

def make_deaths_lst(lst1):
    deaths = []
    for info in lst1:
        deaths.append(info[2])
    return deaths

deaths1 = make_deaths_lst(lst_uscases)

def num_deaths_per_cases(info1, info2):
    average = [int(i)/int(j) for i, j in zip(info1, info2)]
    return average

deaths_per_cases = num_deaths_per_cases(deaths1, cases1)
print(deaths_per_cases)



