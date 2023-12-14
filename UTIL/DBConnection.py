import mysql.connector
from UTIL.PropertyUtil import PropertyUtil  # Correct case sensitivity

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            connection_string = PropertyUtil.getPropertyString()
            try:
                DBConnection.connection = mysql.connector.connect(**connection_string)
                print("Database connected successfully")
            except Exception as e:
                print(f"Error connecting to the database: {e}")
        return DBConnection.connection
