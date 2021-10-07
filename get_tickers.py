import requirements.txt

def get_tickers():
    #stock: empty matrix
    start_date = input('Insert the start date: ')
    end_date = input('Insert the end date: ')
    i = int(input('Insert how many stocks do you want to analyze: '))
    st = []
    stock = []
    st.append(None)
    for x in range(i):
        ask = input('Insert ticker name: ')
        stock.append(ask)
    for x in range(len(stock)):
        st.append(get_data(stock[x],start_date=start_date,end_date=end_date))
    df = pd.concat(st,axis=1)
    return df
