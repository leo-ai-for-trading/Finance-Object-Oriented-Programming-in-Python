import requirements.txt

def max_sp_portfolio():
    
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
    log_stock = log_ret.unstack(level=-1)
    c = []
    i = 0
    while i < len(log_stock.columns):            
        i +=1
        c.append(random.uniform(0,1))
    c = np.array(c)
    allocation = c[:]/sum(c[:])
    #define weights for the allocation
    e_r_ind = log_stock.mean()
    #total expected return
    port_ret = (e_r_ind*allocation).sum()
    exp_cov = log_stock.cov()
    port_var = exp_cov.mul(allocation,axis=0).mul(allocation,axis=1).sum().sum()
    ann_std = log_stock.std()
    assets = pd.concat([e_r_ind,ann_std],axis=1)
    assets.columns = ['log_Return','Volatility']
    p_ret  = []
    p_vol = []
    p_weights = []
    num_assets = len(log_stock.columns)
    num_portfolios = 100
    for portfolio in range(num_portfolios):
        p_weights.append(allocation)
        returns = np.dot(allocation,e_r_ind)
        p_ret.append(returns)
        var =  exp_cov.mul(allocation,axis=0).mul(allocation,axis=1).sum().sum()
        sd = np.sqrt(var)
        ann_sd = sd*np.sqrt(250)
        p_vol.append(ann_sd)
    dataframe = {'Returns':p_ret,'Volatility':p_vol}
    for counter,symbol in enumerate(log_stock.columns.tolist()):
        dataframe[symbol+' weight'] = [allocation[counter] for allocation in p_weights]
    portfolios = pd.DataFrame(dataframe) 
    min_vol_port = portfolios.iloc[portfolios['Volatility'].idxmin()]
    risk_free = 0
    optimal_risky_portf = portfolios.iloc[((portfolios['Returns']-risk_free)/portfolios['Volatility']).idxmax()]
    return optimal_risky_portf

