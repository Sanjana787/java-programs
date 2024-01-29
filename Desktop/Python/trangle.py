import math 
print("enter 3 sides")
a=int(input())
b=int(input())
c=int(input())
s=a+b+c
t1=s-a
t2=s-b
t3=s-c
if(a+b>c) or (b+c>a) or (a+c>b):
    s1=s*t1*t2*t3
    area=math.sqrt(s1)
    print("Area of Triangle is:",area)
else:
  print("Triangle do not exist!!")