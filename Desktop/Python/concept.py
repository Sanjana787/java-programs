class A:
       Avar="class A"
       def __init__(self,namea,pricea) -> None:
            A.Avar
            self.name=namea
            self.price=pricea
       def getname(self):
          return self.name
       def getprice(self):
          return self.price
       def result(self):
            return f"{self.name},{self.price}"
class B():
    Bvar="class B"
    def __init__(self,nameb,priceb) -> None:
          B.Bvar
          self.name=nameb
          self.price=priceb
    def getname(self):
          return self.name
    def getprice(self):
          return self.price
    def result(self):
            return f"{self.name},{self.price}"
       
q=A("sana",77)
p=B("neha",90)
# print(q.Avar,"\n",p.Bvar)
# print(A.Avar)
# print(B.Bvar)
print (q.result())
print(p.result())