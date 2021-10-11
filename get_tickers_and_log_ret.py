import requirements.txt

def get_tickers_and_log_ret():
    
    start_date = input('Insert the start date: ')
    end_date = input('Insert the end date: ')
    i = int(input('Insert how many stocks do you want to analyze: '))
    st = []
    stock = []
    log_ret = [] 
    st.append(None)
    log_ret.append(None)
    for x in range(i):
        ask = input('Insert ticker name: ')
        stock.append(ask)
    for x in range(len(stock)):
        st.append(get_data(stock[x],start_date=start_date,end_date=end_date))   
    df = pd.concat(st,axis=0)
    df.set_index([df.index,'ticker'],inplace=True)
    log_ret = np.log(df['close']/df['open'])
    log_ret = log_ret.unstack(level=-1)
    return df,log_ret
