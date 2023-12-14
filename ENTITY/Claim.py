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

    def addClaim(self):
        self.claimId = int(input('Enter claimId:'))
        self.claimNumber = input('Enter claimNumber:')
        self.dateFiled = input('Enter dateFiled (YYYY-MM-DD):')
        self.claimAmount = float(input('Enter claimAmount:'))
        self.status = input('Enter status:')
        self.policy = input('Enter policy:')
        self.client = int(input('Enter clientId associated with the claim:'))

        data = [
            (self.claimId, self.claimNumber, self.dateFiled, self.claimAmount, self.status, self.policy, self.client)]
        insert_str = '''INSERT INTO Claim(claimId, claimNumber, dateFiled, claimAmount, status, policy, client) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('Claim record inserted successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str = '''SELECT * FROM Claim'''
        self.s.execute(select_str)
        records = self.s.fetchall()
        print('')
        print('Records in Claim Table')
        for i in records:
            print(i)
        self.close()