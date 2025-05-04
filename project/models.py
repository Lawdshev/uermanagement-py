class Loan:
    def __init__(self, id, amount, status, createdAt, user_id):
        self.id = id
        self.amount = amount
        self.status = status
        self.createdAt = createdAt
        self.user_id = user_id

    def to_dict(self):
        return self.__dict__
    
class User:
    def __init__(self, id, username, email, organization, phoneNumber, status, createdAt, password, loans=None):
        self.id = id
        self.username = username
        self.email = email
        self.organization = organization
        self.phoneNumber = phoneNumber
        self.status = status
        self.createdAt = createdAt
        self.password = password
        self.loans = loans if loans is not None else []

    def to_dict(self):
        return self.__dict__
    
    def add_loan(self, loan:Loan):
        self.loans.append(loan)

    def remove_loan(self, loan_id: str):
        self.loans = [loan for loan in self.loans if loan.id != loan_id]

    def get_loans(self)->list[Loan]:
        return self.loans
    
    def get_total_loan_amount(self):
        total = 0
        for x in self.loans:
            total+=x.amount
        return total