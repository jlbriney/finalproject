import matplotlib
import matplotlib.pyplot as plt
import csv
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




#visualization from the calculation
with open('calculations.csv', 'r') as csv_file:
    csv_read = csv.reader(csv_file, delimiter = ',')
    date = []
    num_deaths_per_case = []
    for lines in csv_read:
        date.append(lines[0])
        num_deaths_per_case.append(lines[1])
    date_list = date[1:]
    new_list = num_deaths_per_case[1:]
    new_list = [float(i) for i in new_list]
    
    
    y = date_list
    d1 = new_list
    

    fig, ax = plt.subplots()
    ax.plot(y, d1, 'b-')
    ax.set_xlabel('Date')
    ax.set_ylabel('Rate')
    ax.set_title('COVID-19 Death Rate in US')
    plt.xticks(rotation = 'vertical', fontsize = 4)
    ax.grid()
    # save the line graph
    fig.savefig("test.png")

    # show the line graph
    plt.show()
