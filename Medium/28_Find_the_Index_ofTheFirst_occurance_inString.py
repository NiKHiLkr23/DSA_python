'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
   or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): # early termination
            return -1
        if not needle:
            return 0
    
        i = j = 0
        while j < len(needle) and i < len(haystack): 
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
                continue 
            i += 1
            j += 1
        return i - j if j == len(needle) else -1


#using built-in

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1