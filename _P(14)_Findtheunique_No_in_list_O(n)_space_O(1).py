#Best Solution using XOR operation
arr = [2,2,1,4,4]
ans = arr[0]
for i in range(1,len(arr)):
    ans = ans^arr[i]
print(ans)

#BruteForce approach
arr = [2,2,1,3,3,4]
for i in range(len(arr)):
    chk = False
    for j in range(len(arr)):
        if(i!=j and arr[i]==arr[j]):
            chk = True
            break
    if(chk==False):
        print(arr[i])