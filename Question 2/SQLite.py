"""
    SQLite.py 
    Author: Byrce Streeper
    Date: 3/6/2020

    input: ticker as type string
    output: None
    description: fills an SQL table with price information of a given ticker
"""

#import necessary packages
import sqlite3
import pandas_datareader as pdr
import datetime as dt
import pandas as pd

#create datetime variables to represent the beginning and end of timeframe
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2019,12,31)

#create a sql table
conn = sqlite3.connect('SSMIF.db')
c = conn.cursor()
c.execute("""CREATE TABLE "Stock_Data" (
'Timestamp' INTEGER NOT NULL,
'Open' decimal(10, 2),
'High' deciaml(10, 2),
'Low' deciaml(10, 2),
'Close' deciaml(10, 2),
'Adj_Close' deciaml(10, 2)
);""")

#fill sql table, param: ticker symbol (String), return: None
def Fill_Table(tick):
    df1 = pdr.DataReader(tick, 'yahoo', start, end )

    #iterate through rows of the database
    for index, row in df1.iterrows():

        #convert times to timestamps
        timestamp=dt.datetime.timestamp(index)

        #write database information into the sql table
        sql = "INSERT INTO 'Stock_Data' (Timestamp, Open, High, Low, Close, Adj_Close)\
                 VALUES (%s, %f, %f, %f, %f, %f)"
        values=(timestamp, row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'])
        c.execute(sql % (values))

    #commit the values to the database and closes the cursor
    conn.commit()
    conn.close()

#returns a list of daily returns from the list of close prices
def Daily_Returns(lst):
    ret=[]
    for i in range(len(lst)-1):
        ret.append(lst[i+1]/lst[i]-1)
    return ret

#returns the VaR of the SQL table
def Monthly_VaR(conf=0.05):
    conn = sqlite3.connect('SSMIF.db')
    df = pd.read_sql_query("SELECT Adj_Close FROM Stock_Data", conn)
    df['returns']=[None]+Daily_Returns(df['Adj_Close'])
    df.sort_values('returns', inplace=True)
    
    day_VaR=df['returns'].quantile(conf)
    month_VaR=day_VaR*(252/12)**0.5
    print(df)
    return month_VaR

