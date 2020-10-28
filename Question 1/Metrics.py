"""
    Metrics.py 
    Author: Byrce Streeper
    Date: 3/6/2020

    Daily_Returns
    input: list of size n
    output: list of size n - 1
    description: returns the daily return between 
        individual entries in the given list

    Monthly_VaR
    input: float 
    output: float
    description: returns the VaR of the sql table for 
        a certain confidence level

    Monthly_CVaR
    input: float , string
    output: float
    description: returns the CVaR of the given ticker symbol for 
        a certain confidence level

    Monthly_Volatility
    input: string
    output: float
    description: returns the Volatility of a given ticker in 2019
"""

#import necessary packages
import pandas_datareader as pdr
import datetime as dt
import statistics as st
import sqlite3
import pandas as pd

#create datetime variables to represent the beginning and end of timeframe
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2019,12,31)


#returns a list of daily returns from the data frames 'Adj Close' column
def Daily_Returns(df):
    return df['Adj Close'][:-1].values / df['Adj Close'][1:] - 1

#returns the CVaR of the given ticker during the year 2019
def Monthly_VaR(tick, conf=0.05):
    df = pdr.DataReader(tick, 'yahoo', start, end )
    df['returns']=Daily_Returns(df)
    print(df.head())
    df.sort_values('returns', inplace=True)
   
    day_VaR=df['returns'].quantile(conf)
    month_VaR=day_VaR*(252/12)**0.5
    return month_VaR
    
 #returns the CVaR of the given ticker during the year 2019 
def Monthly_CVaR(tick, conf=0.05):
    df = pdr.DataReader(tick, 'yahoo', start, end )
    df['returns']=Daily_Returns(df)
    df.sort_values('returns', inplace=True)

    day_VaR=df['returns'].quantile(conf)
    day_CVar=st.mean(df['returns'][df['returns']<=day_VaR])
    month_CVar=day_CVar*(252/12)**0.5
    return month_CVar

#returns the Volatility of the given ticker during the year 2019 
def Monthly_Volitility(tick):
    df = pdr.DataReader(tick, 'yahoo', start, end )
    return st.stdev(df['Adj Close'])

Monthly_VaR('AAPL')