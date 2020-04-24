import csv
import sqlite3
import os
import requests
import io
import pandas as pd

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
print(len(deaths_per_cases))

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
print(date_info)


with open('calculations.csv', 'w', newline = '') as f:
    write = csv.writer(f)
    write.writerow(["Date", "Deaths per Cases"])
    write.writerows(zip(date_info, deaths_per_cases))
    f.close()

