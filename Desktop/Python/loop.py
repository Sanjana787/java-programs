# i=10
# while(i>0):
#     print("Everything is possible!!  -->",i) 
#     i-=1
# print("loop executed successfully")


#QUIZ
# i=1
# while i<=50 :
#     print(i)
#     i=i+1


#TO PRINT CONTENT OF A LIST USING WHILE LOOP
# a=["sanjana","saurav","Neha","akash"]
# print(len(a))
# i=0
# while(i<len(a)):
#      print(a[i])
#      i+=1



#PRINTING NAMES USING FOR LOOP
# a=["sanjana","saurav","Neha","akash"]
# for i in a:
#     print(i)



#range function
for i in range(2,22,2):   #it takes n-1 value in range function // to give the starting index to the range function
      #print("-->",i)
      if(i==10):
         #print("its 10")
         continue
      print("-->",i)
else:
         print("this is else")