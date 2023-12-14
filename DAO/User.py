from DAO.connection import DbConnection

class User(DbConnection):

    def __init__(self):
        self.userId = ''
        self.username = ''
        self.password = ''
        self.role = ''

    def create(self):
        create_str = '''CREATE TABLE IF NOT EXISTS User
                (
                    userID INT PRIMARY KEY,
                    userName VARCHAR(200),
                    password VARCHAR(200),
                    role VARCHAR(50)
                )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('User Table created successfully------:')
obj1 = User()
obj1.create()