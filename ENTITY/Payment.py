from DAO.connection import DbConnection

class Payment(DbConnection):
    def __init__(self):
        self.paymentId = ''
        self.paymentDate = ''
        self.paymentAmount = ''
        self.client = ''

    def addPayment(self):
        self.paymentId = int(input('Enter paymentId:'))
        self.paymentDate = input('Enter paymentDate (YYYY-MM-DD):')
        self.paymentAmount = float(input('Enter paymentAmount:'))
        self.client = int(input('Enter clientId associated with the payment:'))

        data = [(self.paymentId, self.paymentDate, self.paymentAmount, self.client)]
        insert_str = '''INSERT INTO Payment(paymentId, paymentDate, paymentAmount, client) VALUES (%s, %s, %s, %s)'''
        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('Payment record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str = '''SELECT * FROM Payment'''
        self.s.execute(select_str)
        records = self.s.fetchall()
        print('')
        print('Records in Payment Table')
        for i in records:
            print(i)
        self.close()