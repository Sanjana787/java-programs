s1=int(input("enter marks of subject 1 : "))
t1=33
m1=(((s1)/90)*100)
if(m1>t1):
    print("pass in subject 1")
else:
    print("fail in subject 1!")
s2=int(input("enter marks of subject 2 : "))
m2=(((s2)/90)*100)
if(m2>t1):
    print("pass in subject 2")
else:
    print("fail in subject 2!")
s3=int(input("enter marks of subject 3 : "))
m3=(((s3)/90)*100)
if(m3>t1):
    print("pass in subject 3")
else:
    print("fail in subject 3!")
total=90
per=40
t=s1+s2+s3
m=((t/90)*100)
if(m>=per):
    print("pass overall")
else:
    print("fail")
