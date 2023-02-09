""" Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice."""

""" Note: This question can be given as arrays are sorted then we can use binary search in that can for efficient solution """

""" Example:Input: nums = [2,7,11,15], target = 9, Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. """


""" Brute force solution:T.C:O(N^2),S.C:O(1)"""
def twosum(arr,target):
    for i in range(len(arr)):
        csum = 0
        for j in range(i,len(arr)):
            csum = arr[i]+arr[j]
            if(csum==target):
                return [i,j]
    return -1
arr = [2,7,11,14]
target = 18
print(twosum(arr,target))

""" Optimum approach : T.C:O(N),S.C:O(N) """
def twoSum(arr,target):
    d = {}
    for i in range(len(arr)):
        if(target-arr[i]) not in d:
            d[arr[i]] = i
        else:
            return [d[target-arr[i]],i]
        
arr = [2,7,11,14]
target = 13
print(twoSum(arr,target))




