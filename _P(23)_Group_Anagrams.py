""" Question:Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""

""" Example:Input: strs = ["eat","tea","tan","ate","nat","bat"] ,Output: [["bat"],["nat","tan"],["ate","eat","tea"]] """
""" Input: strs = [""],Output: [[""]] """

""" Brute force solution using sorting  T.C : O(m*nlog(n)) , S.C:O(n*m)"""
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for i in strs:
            s = str(sorted(i)) # this will return str(list).(i.e sorted() method return list with sort)
            if(s in res):
                res[s].append(i)  # string s is used as key | str(["a","e","t"]:"eat"
            else:
                res[s] = [i]
        return list(res.values())
        
    
"""optimal solution using default dict . to solve duplicate keys problem we can use tuple as key must be unique so if there is same count value then it is appended to same key values.
T.C : O(N*M) | S.C:O(N*M)"""

class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(s)
        return res.values()
