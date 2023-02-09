# code
userinput = 5                                         
first_pattern_value = 1                                
for row in range(userinput):  
    for column in range(row+1):
        print(first_pattern_value,end="")
    first_pattern_value+=1
    print()


# output   
#1
#22
#333
#4444
#55555


#now with this solution we can print all possible combination of pattern!