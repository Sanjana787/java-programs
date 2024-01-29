a=["donkey","monkey"]
with open("new.txt") as f:
    content=f.read()
    print(content)
    for word in a:
       content=content.replace(word,"######")
with open("new.txt","w") as f:
        f.write(content)
        print(content)