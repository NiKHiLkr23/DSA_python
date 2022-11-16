'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for anagrams in strs:
            count = [0]*26
            for word in anagrams:
                count[ord(word)-ord('a')] += 1
            d[tuple(count)].append(anagrams)
        return d.values()