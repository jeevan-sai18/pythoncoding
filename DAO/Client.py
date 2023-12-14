from DAO.connection import DbConnection

class Client(DbConnection):
    def __init__(self):
        self.clientId = ''
        self.clientName = ''
        self.contactInfo = ''
        self.policy = ''

    def create(self):
        create_str = '''CREATE TABLE IF NOT EXISTS Client
        (
        clientId INT PRIMARY KEY,
        clientName VARCHAR(200),
        contactInfo VARCHAR(200),
        policy VARCHAR(50)
        )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('Client Table created successfully------:')
obj2 = Client()
obj2.create()
