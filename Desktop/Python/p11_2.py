class Animals:
    def __init__(self):
       self.bark="barking"
class Pets(Animals):
    def __init__(self):
        var="true value"
class Dog(Pets):
    def bark(self):
        print("Dog barks!!")
a=Dog()
a.bark()