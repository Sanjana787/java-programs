# CALCULATOR
class calc:
    def __init__(self,a,b):
       self.a=a
       self.b=b
    def sum(self):
        return f"sum of the given numbers is {self.a+self.b}"
    def mul(self):
        return f"multiplication of the given numbers is {self.a*self.b}"
    def dev(self):
        return f"division of the given numbers is {self.a/self.b}"
    def sub(self):
        if(self.a>self.b):
          return f"sub of the given numbers is {self.a-self.b}"
        elif(self.b>self.a):
          return f"sub of the given numbers is {self.a-self.b}"


x=int(input("enter first number :"))
y=int(input("enter second number :"))
out=calc(x,y)
print("--------MENU-------- \n 1.ADDITION\n 2.SUBTRACTION\n 3.MULTIPLICATION\n 4.DIVISION\n")
ch=int(input("ENTER YOUR CHOICE::"))
if(ch==1):
   a1=out.sum()
   print(a1)
elif(ch==2):
   a2=out.sub()
   print(a2)
elif(ch==3):
   a3=out.mul()
   print(a3)
elif(ch==4):
  a4=out.dev()
  print(a4)
else:
   print("Invalid Input!!")
