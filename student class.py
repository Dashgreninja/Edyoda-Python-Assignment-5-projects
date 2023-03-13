class Student:
    
    def setName(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber
        
    def getRollNumber(self):
        return self.__rollNumber

# input code to test
obj=Student()
obj.setName('DPS')
obj.setRollNumber(25)
print(f'Name : {obj.getName()}')
print(f'RollNumber : {obj.getRollNumber()}')
