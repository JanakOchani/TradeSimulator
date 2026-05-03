from Trade import Trade
import yfinance as yf
from Database import Database

class TradeHandler:
    trade: Trade


    def __init__(self, l_trade: Trade):
        print(f"TradeHandler: The trade handler for {l_trade.stock} was initialized.")
        self.trade = l_trade #assigned local trade info to the class variable trade so that all methods can access that object with the information.

    def setPrice(self):
        stockdetails = yf.Ticker(self.trade.stock)
        latestPrice = stockdetails.info["regularMarketPrice"]
        self.trade.price = latestPrice
        print(f"TradeHandler: The price for stock {self.trade.stock} is {self.trade.price}.")

    def createQuery(self):
        query = (f"insert into trades (portfolio_name, stock_code, shares, trade_date, action, trade_price) "
                 f"values ('{self.trade.portfolioName}', '{self.trade.stock}', {self.trade.shares}, "
                 f"'{self.trade.tradeDate}', '{self.trade.action}', {self.trade.price})")
        print(f"TradeHandler: The query is {query}.")
        return query



    def saveTrade(self):
        print(f"TradeHandler: About to save trade for stock {self.trade.stock}.")
        query = self.createQuery()
        database = Database()
        database.execute_query(query)

    def executeTrade(self):
        print(f"TradeHandler: About to execute trade for stock.")
        print(f"TradeHandler: The stock ticker is {self.trade.stock}.")

        self.setPrice()
        self.saveTrade()
