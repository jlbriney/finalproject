import csv
import sqlite3
import os

#create three functions 
 
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

us_corona_info = csv_reader('us.csv')

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
    cur.execute("DROP TABLE IF EXISTS USCases")
    cur.execute("CREATE TABLE IF NOT EXISTS USCases(date TEXT, cases INTEGER, deaths INTEGER)") 
    pass

#def write_db(date_data, cases_data, deaths_data): 
 #   try:
    #    conn = sqlite3.connect('/Users/jordanbriney/Desktop/Coronavirus.db')
     #   cur = conn.cursor()
    

        