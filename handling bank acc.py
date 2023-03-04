class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance < amount:
            print('Error : Balance is lower than Withdrawl Amt ')
        else:
            self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def getBalance(self):
        return f'Account Balance : {self.balance}'


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return f'Interest Amount : {(self.balance) * self.interestRate / 100}'


#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object

# printing code to test
demo1.deposit(500)
demo1.withdrawal(700)
print(demo1.interestAmount())
print(demo1.getBalance())