with open("this.txt") as f:
    cont=f.read()

with open("new.txt") as f:
    cont1=f.read() 
    cont1=" "  

with open("new.txt",'w') as f:
    f.write(cont1) 

with open("new.txt") as f:
   a= f.read() 
   print(a)
if cont1==cont:
    print("the two files are identical !")
else:
    print("the two files are not identical")