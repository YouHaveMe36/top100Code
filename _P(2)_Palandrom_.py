# arr = [1,2,3]
# start = 0
# end = len(arr)-1
# while(start<end):
#     arr[start],arr[end] = arr[end],arr[start]
#     start = start+1
#     end = end-1
# print(arr)
    
from errno import ECHILD
from re import I


arr = [10,20,11,23,5]
# m = arr[0]
# i = 0
# while(i<=len(arr)-1):
#     if(m<=arr[i]):
#         m = arr[i]
#     i = i+1
# print(m)
        
# mi = arr[0]
# i = 0
# while(i<=len(arr)-1):
#     if(mi>=arr[i]):
#         mi = arr[i]
#     i = i+1    
# print(mi)
    
# s = arr[0]
# sa = []
# i = 0
# while(i<=len(arr)-1):
#     if(s>=arr[i]):
#         s,arr[i]=arr[i],s
#         sa.append(arr[i])
#     else:
#         sa.append(s)
#     i +=1       
# print(sa)
       
       
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         nums.sort()
#         start = 0
#         end = len(nums)-1
#         while(start<end):
#             sumof = nums[start] + nums[end]
#             if(sumof==target):
#                 return [start,end]
#             elif (sumof<target):
#                 start +=1
#             else:
#                 end -=1       
    
# obj = Solution()
# print(obj.twoSum([3,2,4],6))


# arr = [8,1,7,9,2]
# start = 0
# end = len(arr)-1
# mid = (start+end)//2
# for i in range(0,mid):
#     mxno = arr[0]
#     minno = 0
# def MaxSum(arr,k):
#     start = 0
#     end = 0
#     mxsum = 0
#     windowsum = 0
#     while(end<k):
#         windowsum += arr[end]
#         end +=1
#     while(end<len(arr)):
#         windowsum += arr[end] - arr[start]    
#         mxsum = max(mxsum,windowsum)
#         start +=1
#         end +=1
#     return mxsum

# obj = MaxSum(arr,4)
# print(obj)

# def MaxSum(arr):    
#     start = 0
#     end = len(arr)
#     k = (start+end)//2
#     mxno = arr[0]
#     minno = arr[0]
#     while(start<k):
#         mx = max(mxno,arr[start])
#         mi = min(minno,arr[start])
#         start +=1
#     dif = mx-mi
#     i = k
#     mxno = arr[i]
#     minno = arr[i]
#     for i in range(k,len(arr)):
#         if minno>arr[i]:
#             minno = arr[i]
#         if mxno<arr[i]:
#             mxno = arr[i]
#     diff = mxno-minno
#     return dif + diff
# obj = MaxSum([1,2,1,0,5])
# print(obj)

# arr = [1,2,10,1,5]
# k = 2
# minno = arr[k]
# mxno = arr[k]
# for i in range(k,len(arr)):
#     if minno>arr[i]:
#         minno = arr[i]
#     if mxno<arr[i]:
#         mxno = arr[i]
# print(minno)
# print(mxno)    
 
 
 
# arr = [1,2,3,46,10]
# arr = [1,2,10,1,5]
arr = [-1,4,-2,-3,-7,10,3,9]
assign = arr[0]
assign1 = arr[0]
start = 0
end = len(arr)
mid = (start + end)//2 
assign2 = arr[mid]
assign3 = arr[mid]
while (start<mid):
    if (assign < arr[start]):
        assign = arr[start]
    elif(assign1>arr[start]):
        assign1 = arr[start]
    start = start + 1
print(assign,assign1)
while (mid<end):
    if (assign2 < arr[mid]):
        assign2 = arr[mid]
    elif(assign3>arr[mid]):
        assign3 = arr[mid]
    mid = mid + 1

print(assign2,assign3)
        
      

