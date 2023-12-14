from DAO.connection import DbConnection

class InsuranceServiceImpl(DbConnection):

    def __init__(self):
        super().__init__()

    def calculate_premium(self,client_id):
        premium_amount=1000.0
        return premium_amount

    def file_claim(self,client_id,claim_details):
        claim_id=123
        return claim_id

    def process_claim(self,claim_id):
        result="Claim processed successfully"
        return result

    def make_payment(self,client_id,amount):
        confirmation = "Payment successful"  # Replace with actual payment logic
        return confirmation
    def getter(self):
        print(f"Premium Amount: ${premium}")
        print(f"Claim ID: {claim_id}")
        print(f"Claim Processing Result: {result}")
        print(f"Payment Result: {payment_result}")

insurance_service = InsuranceServiceImpl()

premium = insurance_service.calculate_premium(client_id=123)
claim_id = insurance_service.file_claim(client_id=123, claim_details={'reason': 'Accident'})
result = insurance_service.process_claim(claim_id)
payment_result = insurance_service.make_payment(client_id=123, amount=500.0)


