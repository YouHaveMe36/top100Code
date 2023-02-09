
arr = [1,2,2,2,0,1,1]
s = 0
e = len(arr)-1
while(s<e):
    m = (s+e)//2
    if(arr[m]>arr[e]):
        s = m+1
    else:
        e = m if arr[e] != arr[m] else e - 1
print(arr[s])