import configparser

class PropertyUtil:
    @staticmethod
    def getPropertyString():
        config = configparser.ConfigParser()
        config.read('config.properties')
        # Read connection details from the property file
        hostname = config.get('Database', 'localhost')
        dbname = config.get('Database', 'pycoding')
        username = config.get('Database', 'root')
        password = config.get('Database', 'jeeva')
        port = config.get('Database', '3306')

        # Build the connection string
        connection_string = {
            'host': hostname,
            'database': dbname,
            'user': username,
            'password': password,
            'port': port
        }
        return connection_string
