class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __sub__(self, other):
        if isinstance(other, BankAccount):
            newbalance = self.balance - other.balance
            newaccount = BankAccount(newbalance)
            return newaccount
        return None
    
    def __add__(self, other):
        if isinstance(other, BankAccount):
            newbalance = self.balance + other.balance
            newaccount = BankAccount(newbalance)
            return newaccount
        return None
    def __str__(self):
        return f"BankAccount Balance: {self.balance}"