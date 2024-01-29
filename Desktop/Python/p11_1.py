class c2dvector:
    def __init__(self,i,j):                            #onstructor
       self.icap=i
       self.jcap=j
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
    def run(self):
        print("run run run!!!")
class c3dvector(c2dvector):
   def __init__(self,i,j,k):                            #onstructor
       self.kcap=k
       super().__init__(i,j)
       

   def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
   
   def new():
      print (super().run())
v=c2dvector(12,13)
x=c3dvector(1,2,15)
print(v)
print(x)