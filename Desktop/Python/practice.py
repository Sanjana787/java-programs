class A:
    roll=5
    def __init__(self,aname,aroll):
        self.name=aname
        self.roll=aroll
    def __str__(self):
        return f"name:{self.name}\nroll_no:={self.roll}"
    @classmethod
    def __str__(self) -> str:
        pass
harry=A("harry",7)
# harry.name="harry"
# harry.roll=7
shub=A("sau",9)
print(shub)
print(harry)
# print(A.roll)
# print(shub.__dict__)
# print(A.__dict__)
# print(harry.__dict__)