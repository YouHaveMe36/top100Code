""" Question: Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K."""

""" Example:
Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6. """
""" 
Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1."""

""" Brute force approach: Try every number| T.C:O(n^2) | S.C:O(1)"""
def getPairsCount(arr, n, k):
    count = 0
    for i in range(n):
        csum = 0
        for j in range(i+1,n):
            csum = arr[i]+arr[j]
            if(csum==k):
                count+=1
    return count


""" Optimum approach:Use hashmap just like two sum approach|T.C:O(N)|S.C:O(N)"""
def getPairsCount(arr, n, k):
    d = {}
    count = 0
    for i in range(len(arr)):
        if(k-arr[i]) in d:
            count+=d[k-arr[i]]
            if(arr[i]) in d:
                 d[arr[i]] +=1
            else:
                 d[arr[i]]=1
    return count

