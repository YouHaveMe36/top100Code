""" Question:-
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.#
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums. """

#Example:-
""" Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2. """


""" Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6. """


#Code :- use hashmap for frequency store start value and end value of element whose frequency is maximum then substract (end value - start value+1).
# append that value to a list then return the min of that list [i.e if more then one element has same frequency]
""" T.c : O(n)
S.c : O(n) due to hashmap """
arr = [1,2,2,3,1,4,2]
frequency = {}
start = {}
end = {}
def degree(arr):
    for i in range(len(arr)):
        if arr[i] not in frequency:
            frequency[arr[i]] = 1
            start[arr[i]]=i
            end[arr[i]] =i
        else:
            frequency[arr[i]]+=1
            end[arr[i]]=i
    maxi = max(frequency.values())
    result = []
    for i,j in frequency.items():
        if (j==maxi):
            total = end[i]-start[i]+1
            result.append(total)
    return min(result)

obj = degree(arr)
print(obj)
            


