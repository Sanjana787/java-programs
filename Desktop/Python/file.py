# f=open('sample.txt','r')
# data=f.read()
# print(data)
# print(f"{data}")
# f.close()
# f=open("sample.txt","w")
# sen="i miss you"
# f.write(sen)
# f.close()
# f=open('sample.txt','r')
# data=f.read()
# print(f"{data}")
# f.close()
with open("sample.txt","a") as f:
    sen="i miss you"
    f.write(sen)

with open('sample.txt','r') as f: 
   data=f.read()
   print(f"{data}")
 