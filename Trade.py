class Trade:
    def __init__(self, l_stock, l_shares, l_portfolioName, l_tradeDate, l_action):
        self.stock = l_stock
        self.shares = l_shares
        self.portfolioName = l_portfolioName
        self.tradeDate = l_tradeDate
        self.action = l_action
        self.price = 0.0

        print(f"Trade: The tradeInfo object for {self.stock} was intialized.")
        print(f"Trade: The tradeInfo object for {self.shares} was intialized.")
        print(f"Trade: The tradeInfo object for {self.portfolioName} was intialized.")
        print(f"Trade: The tradeInfo object for {self.tradeDate} was intialized.")
        print(f"Trade: The tradeInfo object for {self.action} was intialized.")






