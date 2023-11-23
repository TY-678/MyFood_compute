import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def sql_connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='xxxx',
            password='xxxx',
            database='MyFood'
        )
        self.cursor = self.connection.cursor()

    def sql_close(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
