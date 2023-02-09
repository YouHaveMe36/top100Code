
#upper hill pattern 
userinput = 5
for row in range(userinput):
    for column in range(row,userinput):
        print(" ",end="")
    for column in range(row+1):
        print("*",end="")
    for column in range(row):
        print("*",end="")
    print()
    
print('\n')


#reverse hill pattern
userinput = 5
for row in range(userinput):
    for column in range(row+1):
        print(" ",end="")
    for column in range(row,userinput):
        print("*",end="")
    for column in range(row,userinput-1):
        print("*",end="")
    print()
    
