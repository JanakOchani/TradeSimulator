1) Used the terminal to install the packages of yfinance, psycopg2-binary, 
uvicorn (web server) and fastapi. 

2) Created a repository on GitHub and called it TradeSimulator, and committed the packages
to the repository. 

3) How to start webserver: use the command uvicorn tradeapi:tradeSimulator --reload. tradeapi is the name of the Python file that has apis, and tradeSimulator is the root route.

4) To test root, go to browser and past in the URL, or run it with the terminal command: curl -X GET -H "Content-Type: application/json" 'http://localhost:8000/'        

5) New route for post: curl -X POST -H "Content-Type: application/json" 'http://localhost:8000/tradestock?stock=AMZN'. More parameters must be separated with an "&".
For example: curl -X POST -H "Content-Type: application/json" 'http://localhost:8000/tradestock?stock=AMZN&shares=100&portfolioName=JANAK&tradeDate=2026-05-02&action=BUY'

After this, a Trade class was created with all of the different information of the stock to be processed, such as the ticker, the number of shares, the name of the portfolio,
the date of the transaction, the action (buy or sell), and the price. 

The TradeHandler class was created which stores all of the methods of the project, such as executing and saving the trade, setting the price
of the stock (I used the latest market price of the stock, not the actual price of the stock at inputted date), and creating the query. 

The query, written in SQL, was ultimately linked to the newly made Database class, which holds all of the properties required to open the connection and store the trade. 



