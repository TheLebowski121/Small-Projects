import datetime as DTE
import matplotlib.pyplot as PLT
import matplotlib.style as STYLE
import pandas as PD
import pandas_datareader.data as web
# Here we are telling the program to computer to make the codes in these availabe to the current program
start = DTE.datetime(2000, 1, 1)
end = DTE.datetime(2016, 12, 31)
# We will use these dates to to fetch data for (TSLA) from Yahoo Finance API
DF = web.DataReader('TSLA','yahoo', start, end)
print(DF.head())
# DF is pandas Data Frame that contains the data for Tesla. Well use 'DF.head()' to print the first few rows of the data frame
# A data Frame is a two-Dimensional table of data with columns of potentially diffrent types. It is similar to an Excel spreadsheet or a table in a relational database.
quarterTwo = stock_data['earnings']['earningsChart']['quarterly'][0]['actual']['raw']