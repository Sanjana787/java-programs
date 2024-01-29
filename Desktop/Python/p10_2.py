import numpy as np
class calculator:
    def __init__(self,num):
        self.n=num
    def cube(self):
        
        print (self.n**3)
    def sq(self):
        print (self.n**2)
    def sqrt1(self):
        print(np.sqrt(self.n))
    
#x=int(input("Enter a number:"))
y=calculator(4)
y.cube()
y.sqrt1()
y.sq()
#print(f"cube of the number is:{z}")