import pandas as pd
import numpy as np
from datetime import datetime
import csv
import matplotlib.pyplot as plt

WINDOWS = 7;
confirmed_df = pd.read_csv("../covid_prediction_data/confirmed_cases.csv")
deaths_df = pd.read_csv("../covid_prediction_data/confirmed_deaths.csv")


# Showing total confirmed cases 
# plt.plot( confirmed_df['date'], confirmed_df['total_ca
# plt.show()



# Showing total death cases 
# plt.plot( deaths_df['date'], deaths_df['total_deaths'])
# plt.show()

# Showing total death cases and total confirmed cases
# plt.plot( deaths_df['date'], deaths_df['total_deaths'],confirmed_df['total_cases'])
# plt.show()

total_cases =  confirmed_df['total_cases'].sum() 
total_death_cases = deaths_df['total_deaths'].sum();
mortality_rate = total_death_cases/total_cases 


def daily_increase(data):
    d = [] 
    for i in range(len(data)):
        if i == 0:
            d.append(data[0])
        else:
            d.append(data[i]-data[i-1])
    return d 

def moving_average(data, window_size):
    moving_average = []
    for i in range(len(data)):
        if i + window_size < len(data):
            moving_average.append(np.mean(data[i:i+window_size]))
        else:
            moving_average.append(np.mean(data[i:len(data)]))
    return moving_average

def country_plot(x, y1, y2, y3, country):
    # window is set as 14 in in the beginning of the notebook 
    confirmed_avg = moving_average(y1, WINDOWS)
    confirmed_increase_avg = moving_average(y2, WINDOWS)
    death_increase_avg = moving_average(y3, WINDOWS)
#     recovery_increase_avg = moving_average(y4, window)
    
    plt.figure(figsize=(16, 10))
    plt.plot(x, y1)
    plt.plot(x, confirmed_avg, color='red', linestyle='dashed')
    plt.legend(['{} Confirmed Cases'.format(country), 'Moving Average {} Days'.format(WINDOWS)], prop={'size': 20})
    plt.title('{} Confirmed Cases'.format(country), size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(x, y2)
    plt.plot(x, confirmed_increase_avg, color='red', linestyle='dashed')
    plt.legend(['Moving Average {} Days'.format(WINDOWS), '{} Daily Increase in Confirmed Cases'.format(country)], prop={'size': 20})
    plt.title('{} Daily Increases in Confirmed Cases'.format(country), size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(x, y3)
    plt.plot(x, death_increase_avg, color='red', linestyle='dashed')
    plt.legend(['Moving Average {} Days'.format(WINDOWS), '{} Daily Increase in Confirmed Deaths'.format(country)], prop={'size': 20})
    plt.title('{} Daily Increases in Deaths'.format(country), size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()
