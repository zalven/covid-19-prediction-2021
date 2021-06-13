

import pandas as pd
import numpy as np


DIRECTORY = '../covid_prediction_data/'

def confirmed_cases( inp, out , columns ):
    inp = DIRECTORY+inp
    out = DIRECTORY+out
    confirmed_df = pd.read_csv( inp ) 
    confirmed_case = pd.DataFrame( confirmed_df, columns=columns)
    confirmed_case.to_csv(out,index=False )


def latest_data( inp, out  ):
    inp = DIRECTORY+inp
    out = DIRECTORY+out
    confirmed_df = pd.read_csv(inp) 
    latest_date = pd.to_datetime(confirmed_df['date']).max()
    latest_case = confirmed_df [ pd.to_datetime(confirmed_df['date'])== latest_date ] 
    latest_case.to_csv(out, index=False )


def extract_data( inp, out ):
    inp = DIRECTORY+inp
    out = DIRECTORY+out
    cases = pd.read_csv(inp)
    cases = cases[  cases['iso_code'] == 'PHL' ] 
    cases.to_csv( out, index=False )

def covid_ph_data_extraction():
    extract_data('owid-covid-data.csv' , "philippines_covid_cases.csv")
    confirmed_cases( "philippines_covid_cases.csv", "confirmed_cases.csv" ,[ 'iso_code','continent','location','date','total_cases'] )
    confirmed_cases( "philippines_covid_cases.csv", "confirmed_deaths.csv", [ 'iso_code','continent','location','date','total_deaths'])
    latest_data( "philippines_covid_cases.csv", "latest_case.csv")


if __name__ == '__main__':
    covid_ph_data_extraction()



# arima = ARIMA(data['y'], order=(5, 1, 0))
# arima = arima.fit(trend='c', full_output=True, disp=True)
# forecast = arima.forecast(steps= 30)
# pred = list(forecast[0])

# start_date = data['ds'].max()
# prediction_dates = []
# for i in range(30):
#     date = start_date + datetime.timedelta(days=1)
#     prediction_dates.append(date)
#     start_date = date
# plt.figure(figsize= (15,10))
# plt.xlabel("Dates",fontsize = 20)
# plt.ylabel('Total cases',fontsize = 20)
# plt.title("Predicted Values for the next 15 Days" , fontsize = 20)

# plt.plot_date(y= pred,x= prediction_dates,linestyle ='dashed',color = '#ff9999',label = 'Predicted');
# plt.plot_date(y=data['y'],x=data['ds'],linestyle = '-',color = 'blue',label = 'Actual');
# plt.legend();

# import pandas as pd
# import numpy as np
# import datetime
# import requests
# import warnings

# import matplotlib.pyplot as plt
# import matplotlib
# import matplotlib.dates as mdates
# import seaborn as sns
# import squarify
# import plotly.offline as py
# import plotly_express as px

# from xgboost import XGBRegressor
# from lightgbm import LGBMRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.svm import SVR
# from sklearn.metrics import mean_squared_error, mean_absolute_error
# from sklearn.preprocessing import OrdinalEncoder
# from sklearn.svm import SVR
# from sklearn.model_selection import train_test_split
# from statsmodels.tsa.arima_model import ARIMA
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly, add_changepoints_to_plot