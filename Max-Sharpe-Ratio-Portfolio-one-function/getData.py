
def getData(tickers,i):
  #tickers is an empty list
  #i: numbers of ticker 
    for x in range(i):
        ask = input('Insert a ticker: ')
        tickers.append(ask)
    data = yf.download(tickers, period='ytd',interval='1d',auto_adjust=True,
    group_by='ticker')
    print(data)
    return data
