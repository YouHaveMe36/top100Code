
#Navie approach: T.C:O(k*n)

arr = [1,2,3,4,5]
p1 = len(arr)-1
p2 = len(arr)-2
k=2
while(k>0):
    while(p1>0 and p2>-1):
        arr[p1],arr[p2] = arr[p2],arr[p1]
        p1-=1
        p2-=1
    p1 = len(arr)-1
    p2 = len(arr)-2
    k-=1
print(arr)


#optimum approach : T.C:O(n)
nums = [1,2,3,4,5,6,7]
k = 3
if(k>len(nums)):
    k = k%len(nums)
    nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]
else:
    nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]
print(nums) 
