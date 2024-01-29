# def fun1(s):
#     print("hello " + str(s))

# a=input("enter your name :")
# fun1(a)


#program to find greatest of three numbers

# def great(n1,n2,n3):
#     if(n1>n2):
#        f=n1 
#     else:
#         f=n2 
#     if(f>n3):
#         print("greatest number is "+str(f))
#     else:
#          print("greatest number is "+str(n3))
    
# num1:(input("enter number 1"))
# num2:(input("enter number 2"))
# num3:(input("enter number 3"))
# #great(6,9,10)
# # great(int(num1),int(num2),int(num3))


# def far(c):
#     return(c*(9/5)+32)
# c=0
# d=far(c)
# print("temperature is "+str(d)+"fahreheit")


#SUM OF FIRST N NATURAL NUMBERS
# def Sum(n):
#     # if(n==0):
#     #   return 0
    
#        return(n*((n+1)/2))
# n=-10
# s=Sum(n)
# print("sum is:"+str(s))



# def total(n):
#      if(n==0):
#         return 0
#      else:
#           return(n)+total(n-1)
# n=5
# f=total(n)
# print("sum is :"+str(f))



# n=3
# for i in range(3):
#     print("*"*(n-i))


#to convert inches to cm
# def cm(i):
#     return (i*2.54)
# i=20
# c=cm(i)
# print(f"the value of {i} in cm is:{c}")



#to remove a word in a string
# def re(string,word):
#     new=string.replace(word," ")
#     return new. strip()
# string="hello sanjana its shiva"    
# n=re(string,"hello")
# print(n)



def table(n):

    for i in range(1,10):
        print(f"{n}*{i}={n*i}")
n=10
t=table(n)
