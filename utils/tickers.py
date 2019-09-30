import pandas_datareader as pdr
import datetime
import pandas as pd

def get_tickers(tickers, startdate=(datetime.datetime.today() - datetime.timedelta(days=365*2)), enddate=datetime.datetime.today()):
  def data(ticker):
    return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))