class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance
class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
savings_acc = SavingsAccount("Ashish", 5000, 5)
print(savings_acc.title)         
print(savings_acc.balance)       
print(savings_acc.interestRate)  

        
