#Now let's just try to programe a diamnond pattern now 

# upper part of that(common part of diamond not included in this we need to run the loop (n-1) times for that i.e n=userinput) 
userinput = 5
for row in range(userinput-1):
    for column in range(row,userinput):
        print(" ",end = "")
    
    for column in range(row+1):
        print("*",end="")
    
    for column in range(row):
        print("*",end="")
    print()
#Lower part of that(common part of diamond  included in this we need to run the loop (n) times for that i.e n=userinput)   
for row in range(userinput):
    for column in range(row+1):
        print(" ",end="")
    
    for column in range(row,userinput):
        print("*",end="")
        
    for column in range(row,userinput-1):
        print("*",end="")
    print() 