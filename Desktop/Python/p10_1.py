class programmer:
    company="Microsoft"
    def __init__(self,name,branch,project) :
       self.name=name
       self.project=project
       self.branch=branch
    def info(self):
        print(f"Employee Information ::\n Name:{self.name} \n Branch:{self.branch} \n Project currently working on:{self.project} in {self.company} ")
    @staticmethod
    def i():
      print("Thanks!")
sanjana=programmer("Sanjana","hyderabad","game")
neha=programmer("Neha","hyderabad","app_development")
sanjana.info()

neha.info()