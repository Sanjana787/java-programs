text=input("enter your text")
spam=False
if("watch your words" in text):
    spam=True
if("let it go" in text):
    spam=True
if("be careful this time" in text):
    spam=True
if("i don't beleive this" in text):
    spam=True
else:
    spam=False
if(spam):
     print("this text is a spam")
else:
    print("it's not a spam")