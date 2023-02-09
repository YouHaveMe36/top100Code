arr = [1,2,3,3,4,4,4,4,5,8,23,7]
def binary(arr,num):
    start = 0
    end = len(arr)-1
    ans = -1
    while(start<=end):
        mid = (start+end)//2
        if (arr[mid]<=num):
            ans = mid
            start=mid+1
        else:
            end = mid-1
    return ans

check = binary(arr,4)
print(check) 