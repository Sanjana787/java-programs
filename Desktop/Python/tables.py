
for j in range(2,21):
    with open (f"table_of_{j}.txt",'w') as f:
         for i in range (1,11):
             f.write(f"{j}X{i}={j*i}")
             if i!=10:
              f.write("\n")
    
