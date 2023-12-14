from DAO.connection import DbConnection

class Claim(DbConnection):
    def __init__(self):
        self.claimId = ''
        self.claimNumber = ''
        self.dateFiled = ''
        self.claimAmount = ''
        self.status = ''
        self.policy = ''
        self.client = ''

    def create(self):
        create_str = '''CREATE TABLE IF NOT EXISTS Claim
                        (
                            claimId INT PRIMARY KEY,
                            claimNumber VARCHAR(200),
                            dateFiled DATE,
                            claimAmount DECIMAL(10, 2),
                            status VARCHAR(50),
                            policy VARCHAR(50),
                            client INT,
                            FOREIGN KEY (client) REFERENCES Client(clientId)
                        )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('Claim Table created successfully------:')
obj3 = Claim()
obj3.create()