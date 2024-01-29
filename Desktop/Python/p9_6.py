with open("log.txt") as f:
   d= f.read()
if "python" in d:
   print("python is present!!")
   
else:
   print("python is absent")