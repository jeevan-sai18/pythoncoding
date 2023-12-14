from DAO.connection import DbConnection

class Payment(DbConnection):
    def __init__(self):
        self.paymentId = ''
        self.paymentDate = ''
        self.paymentAmount = ''
        self.client = ''

    def create(self):
        create_str = '''CREATE TABLE IF NOT EXISTS Payment
                        (
                            paymentId INT PRIMARY KEY,
                            paymentDate DATE,
                            paymentAmount DECIMAL(10, 2),
                            client INT,
                            FOREIGN KEY (client) REFERENCES Client(clientId)
                        )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('Payment Table created successfully------:')
obj4 = Payment()
obj4.create()
