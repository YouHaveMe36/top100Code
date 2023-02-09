# Question :- Given an integer array nums, find the subarray with the largest sum, and return its sum.
""" Example:-
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6. """

#code :- we can just simply take the element one by one and sum it all till the end if the sum if greater the 0 the continue other wise move to next element.

#brute force :-
arr =  [-2,1,-3,4,-1,2,1,-5,4]
csum = 0
msum = arr[0] # as their are negative no. present so we need to takt the first value of an array as maximum sum (i.e [-4,-2,-1]  msum = -1)
for i in range(len(arr)):
    csum = 0
    for j in range(i,len(arr)):
        csum+=arr[j]
        msum = max(csum,msum)
print(msum)


#optimum solution
for i in arr:
    if(csum<0):
        csum = 0
    csum+=i
    msum = max(csum,msum)
print(msum)
