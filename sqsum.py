class Point:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sum=0
        for i in (self.x,self.y,self.z):
            i**=2
            sum+=i
        return sum
    
# input code to test
sample = Point(1,3,5)
print(sample.sqSum())