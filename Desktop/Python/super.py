class A:
    classvar="IN A"
    def __init__(self) :
     self.classvar="INSIDE CONSTRUCTOR OF A"
     self.passion="INDIAN AIR FORCE"
    def sanjana(self):
        self.var="BE RUTHLESS TO THOSE WHO DESERVE IT "
        print(self.classvar)
class B(A):
    classvar="IN B"
    def __init__(self) :
      super().__init__()
      self.classvar="INSIDE CONSTRUCTOR OF B"         #instance variable
      

x=A()
y=B()
print( x.classvar,"\n")
print(y.passion,"\n")
print( y.classvar,"\n")
print( x.sanjana(),"\n")
