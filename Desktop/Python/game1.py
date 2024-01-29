# GAME OF STONE ,PAPER AND SCISSOR
import random 

def game(ch,c):  
  
  if(ch=="s"):
      if(c=='w'):
         return True
      elif(c=='g'):
         return  False

  elif(ch=="w"):
      if(c=="g"):
         return True
      elif(c==s):
         return  False 
  elif(ch=="g"):
      if(c=="s"):
         return True
      elif(c=="w"):
         return  False
  elif(ch==c):
     return None

print("computer turn : snake(s),water(w) or gun(g)")
randno=random.randint(1,3)

print(randno)
if(randno==1):
   c="s"
elif(randno==2):
   c="w"
elif(randno==3):
   c="g"  

ch=input("your turn : snake(s),water(w) or gun(g)")
print(f"computer choose :{c} and you chose : {ch}")
a=game(ch,c)
if(a==True):
   print("YOU WIN!!")
elif(a==False):
   print("COMPUTER WIN!!")
elif(a==None):
   print("IT'S A TIE!!")
