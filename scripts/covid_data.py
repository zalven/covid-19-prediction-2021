

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
    pass 
    #  Uncommen the function for data resets
    covid_ph_data_extraction()

