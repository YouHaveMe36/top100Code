
#for increasing triangle
# userinput=5
# for row in range(userinput):
#     for column in range(row+1):
#         print(column+1,end="")
#     print()
    
    
print("\n")


# userinput = 5
# for row in range(userinput):
#     for column in range(row,userinput):
#         print(column+1,end="")
#     print()



n=5
for row in range(n):
    p = 1
    for column in range(row,n):
        print(" ",end="")
    for column in range(row+1):
        print(p,end="")
        p+=1
    for column in range(row):
        print(p,end="")
        p+=1
    print()