userinput = 5
#uppper side of butterfly pattern 
for row in range(userinput-1):
    for column in range(row+1):
        print("*",end="")        #This will print output on one single line
    for column in range(row,userinput-1):
        print(" ",end="")
        
    for column in range(row,userinput-1):
        print(" ",end="")

    for column in range(row+1):
        print("*",end="")     
    print()  

#lower side of butterfly pattern        
for row in range(userinput):       
    for column in range(row,userinput):
        print("*",end="")        #This will print output on one single line
#Center space
    for column in range(row):
        print(" ",end="")
    for column in range(row):
        print(" ",end="")
    for column in range(row,userinput):
        print("*",end="") 
    print()