# name=input("enter a name:")
# pre=" good afternoon"
# print(name+pre )
dear="sanjana"
date="28-4-23"
letter="Dear <dear>,\n \tyou  are  selected!\n<date>"
letter=letter.replace("<dear>",dear)
letter=letter.replace("<date>",date)
print(letter.find("  "))
print(letter.count("  "))
letter=letter.replace("  "," "  )
print(letter)