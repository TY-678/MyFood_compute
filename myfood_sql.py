import psycopg2


class DatabaseConnector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def sql_connect(self):
        self.connection = psycopg2.connect(
            host="localhost",
            port="5432",
            user="ty",
            password="tymacminipassword",
            database="my_food",
        )
        self.cursor = self.connection.cursor()

    def sql_close(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
