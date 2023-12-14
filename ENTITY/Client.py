from DAO.connection import DbConnection

class Client(DbConnection):
    def __init__(self):
        self.clientId = ''
        self.clientName = ''
        self.contactInfo = ''
        self.policy = ''

    def addClient(self):
        self.clientId = int(input('Enter clientId:'))
        self.clientName = input('Enter clientName:')
        self.contactInfo = input('Enter contactInfo:')
        self.policy = input('Enter policy:')
        data = [(self.clientId, self.clientName, self.contactInfo, self.policy)]
        insert_str = '''INSERT INTO Client(clientId, clientName, contactInfo, policy) VALUES (%s, %s, %s, %s)'''
        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('Client record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str = '''SELECT * FROM Client'''
        self.s.execute(select_str)
        records = self.s.fetchall()
        print('')
        print('Records in Client Table')
        for i in records:
            print(i)
        self.close()