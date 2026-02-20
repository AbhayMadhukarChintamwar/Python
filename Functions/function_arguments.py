
def company_info(**kwargs):
    if 'ticker' in kwargs:
        print("Ticker:", kwargs['ticker'])    
    if 'ceo' in kwargs:
        print("CEO:", kwargs['ceo'])    
    if 'revenue' in kwargs:
        print("Revenue:", kwargs['revenue'])


company_info(ticker = "AAPL", ceo = "Tim Cook", revenue = "$114.7B", market_cap = "2.5T")
