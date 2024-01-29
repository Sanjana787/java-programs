import time

class student:
      standard=10
      Name=" "
      section=" "
      roll=''
      def info(self) :
       print(f"Name of student is {self.Name} and roll number is {self.roll} studying in class {self.standard}")
      @staticmethod
      def greet():
          print("GOOD MORNING!")
      @staticmethod
      def tim():
          localtime=time.asctime(time.localtime(time.time()))
          print("TIME IS ",localtime)

stu=student()
stu.Name="Sanjana"
stu.section="A"
stu.roll=77
stu.info()
stu.greet()
stu.tim()