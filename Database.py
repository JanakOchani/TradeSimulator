import psycopg2

class Database:
    def __init__(self):
        print(f"Database object initialized.")

    def execute_query(self, query: str):
        try:
            connection = self.getConnection()
            print(f"Database: DB connection object is {connection}.")
            print(f"Database: About to execute query {query}.")

            editor = connection.cursor()
            editor.execute(query)
            connection.commit()

            editor.close()
            connection.close()

        except Exception as my_error:
            print(f"Database: The error while executing the query was {my_error}.")


    def getConnection(self):
        connection = psycopg2.connect(host='localhost', port='5432', database='trade_simulator', user='postgres', password='postgres')
        return connection



