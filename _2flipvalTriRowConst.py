# code:-
userinput = 5
first_value_of_row = 5
for row in range(userinput):
    for column in range(row+1):
        print(first_value_of_row,end="")
    first_value_of_row -=1
    print()

#output:-
# 5
# 44
# 333
# 2222
# 11111  


print("\n")

userinput = 5
for row in range(userinput):
    for column in range(row+1):
        if(column%2!=0):
            print(2,end="")
        
        else:
            print(1 ,end="")
    print()