arr = [1,2,3,3,4,4,4,4,4,4,5,5,8,8,23,7]
def binary(arr,num):
    start = 0
    end = len(arr)-1
    ans = -1
    while(start<=end):
        mid = (start+end)//2
        if (arr[mid]>=num):
            ans = mid
            end = mid-1
        elif(arr[mid]<num):
            start = mid+1
    return ans

check = binary(arr,8)
print(check) 