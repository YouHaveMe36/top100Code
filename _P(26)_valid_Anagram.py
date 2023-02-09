""" Question:- Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. """

""" Example: Input: s = "anagram", t = "nagaram" Output: true 
    Input: s = "rat", t = "car"Output: false"""

"""Intution : we can use either count method for brute force approach. A better approach would be use hashmap.Create two hashmap then compare the frequency of every element in it."""

# Code:
# Brute force approach: T.C:O(N^2),S.C:O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        for i in s:
            if(s.count(i)!=t.count(i)):
                return False
        return True

#Optimum approach: T.C:O(N), S.C:O(N)
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        d = {}
        c = {}
        for i in range(len(s)):
            if(s[i] not in d):
                d[s[i]]=1
            else:
                d[s[i]]+=1
        for i in range(len(t)):
            if(t[i] not in c):
                c[t[i]]=1
            else:
                c[t[i]]+=1
        for i in d:
            if(d.get(i)!=c.get(i)):
                return False
        return True


