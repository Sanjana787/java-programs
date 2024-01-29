def game():
    return 990
score=game()
with open("hiscore.txt") as f:
    hiscore=f.read()
    if(hiscore==" " or int(hiscore)<score):
       with open("hiscore.txt","w") as f:
         score=str(score)
         f.write(str(score))
       with open("hiscore.txt") as f:
          d=f.read()
          print("NEW HIGH SCORE IS:: "+str(d))
    elif(int(hiscore)>=score):
       with open("hiscore.txt") as f:
          d=f.read()
          print("HIGH SCORE IS:: "+str(d))
#with open("highscore.txt","r") as f:
