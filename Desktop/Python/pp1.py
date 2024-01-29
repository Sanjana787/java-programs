age=int(input("enter your age or birth year"))
if(age<=100):
    print("number of years left for person to be aged 100::",100-age)
elif(age>100):
    # rem=age%100
    # year=100-rem
    age+=100
    print(age)
    