class Student:
    
    def setName(self,name):
        self.name=name
        
    def getName(self):
        return f'Name : {self.name}'
    
    def setRollNumber(self,rollNumber):
        self.rollNumber=rollNumber
        
    def getRollNumber(self):
        return f'rollNumber : {self.rollNumber}'

# input code to test
obj=Student()
obj.setName('DPS')
obj.setRollNumber(25)
print(obj.getName())
print(obj.getRollNumber())