#first no. greater > x:~
arr = [1,3,5,5,5,5,7,9,10]
start = 0
end = len(arr)-1
x = 1
ub = len(arr)       
while(start<=end):
    mid = start + (end-start)//2
    if(arr[mid]<=x):
        start = mid+1
    else:
        ub = mid
        end = mid-1
print(arr[ub])