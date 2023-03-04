class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        

# input code to test

obj=Account("Ashish", 5000)
print(obj.balance,obj.title)
obj2=SavingsAccount("Ashish", 5000, 5)
print(obj2.balance,obj2.title,obj2.interestRate)

