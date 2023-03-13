class Calculator:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num2 / self.num1

# input code to test  
obj = Calculator(10,94)
print(f'sum of numbers : {obj.add()}')
print(f'difference of numbers : {obj.subtract()}')
print(f'multiplication of numbers : {obj.multiply()}')
print(f'division of numbers : {obj.divide()}')
