import requirements.txt

def get_tickers(i,start_date,end_date):
    #obtain n stocks
    stock = []
    st = []
    st.append(None)
    for x in range(i):
        ask = input('Insert ticker name: ')
        stock.append(ask)
    for x in range(len(stock)):
        st.append(get_data(stock[x],start_date=start_date,end_date=end_date))
    df = pd.concat(st,axis=1)
    return df
