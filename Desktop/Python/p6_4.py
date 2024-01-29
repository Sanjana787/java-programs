# f=input("enter your name")
# print(len(f))
# if(len(f)>10):
#     print("greter")

# else:
#     print("lesser")


# a=["saurav","kaithal","sirsa","chambal"]
# text=input("enter the text")
# if(text in a):
#     print("it is present")
# else:
#     print("it is absent")



# marks=int(input("enter your marks:"))
# if marks >= 90:
#       grade='Ex'
# elif marks>=80:
#       grade='A'
# elif marks>=70:
#       grade='B'
# elif marks>=60:
#       grade='C'
# elif marks>=50:
#       grade='D'
# else:
#       grade='F'

# print("your grade is :"+ grade)




post='''hi !
        hope you are doing well,
        missed you at lunch.
        by HaRRy'''
print(post.count("harry"))
if(post.find("harry")>0):
    print("it is about harry")
else:
    print("it's not  about harry")