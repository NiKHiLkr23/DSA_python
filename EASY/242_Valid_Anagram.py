'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all 
the original letters exactly once.'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_count = [0]*26
        sum_=0
        for i in s:
            char_count[ord(i)-ord("a")] += 1
        for j in t:
            char_count[ord(j)-ord("a")] -= 1
        for i in range(26):
            sum_ += abs(char_count[i])
        return sum_==0