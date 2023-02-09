""" Question :- Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. """
""" Example :- Input: nums = [1,2,3,1] Output: true """

"""Instution :- Using Hashmap to count the frequency and then return the bool value  """ 

# Code :-
class Solution:
    def containsDuplicate(self,nums):
        d = {}
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]]=1
            else:
                return True
        return False