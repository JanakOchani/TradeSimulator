from fastapi import FastAPI
from Trade import Trade
from datetime import date
from TradeHandler import TradeHandler

tradeSimulator = FastAPI()

@tradeSimulator.get("/")
def root():
    print(f"Request received for homepage.")
    return {"Hello": "tradeSimulator"}

@tradeSimulator.post("/tradestock")
def tradeStock(stock: str, shares: int, portfolioName: str, tradeDate: date, action: str):
    tradeInfo = Trade(stock, shares, portfolioName, tradeDate, action)
    handler = TradeHandler(tradeInfo)
    handler.executeTrade()
    print(f"tradeapi: About to process the trade: {handler}.")

    print(f"tradeapi: The stock to be traded is {tradeInfo.stock}.")
    print(f"tradeapi: The number of shares is {tradeInfo.shares}.")
    print(f"tradeapi: The portfolio name is {tradeInfo.portfolioName}.")
    print(f"tradeapi: The date of the trade is {tradeInfo.tradeDate}.")
    print(f"tradeapi: The action requested is {tradeInfo.action}.")

    return {f"Stock": {tradeInfo.stock}, "Shares": {tradeInfo.shares}}


