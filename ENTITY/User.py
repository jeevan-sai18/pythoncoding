from DAO.connection import DbConnection

class User(DbConnection):

    def __init__(self):
        self.userId = ''
        self.username = ''
        self.password = ''
        self.role = ''


    def addUser(self):
        self.userId = int(input('Enter userId:'))
        self.username = input('Enter username:')
        self.password = input('Enter password:')
        self.role = input('Enter role:')
        data = [(self.userId, self.username, self.password, self.role)]
        insert_str = '''INSERT INTO User(userId, username, password, role) VALUES (%s, %s, %s, %s)'''
        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('User record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str = '''SELECT * FROM User'''
        self.s.execute(select_str)
        records = self.s.fetchall()
        print('')
        print('Records in User Table')
        for i in records:
            print(i)
        self.close()


