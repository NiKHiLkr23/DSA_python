'''A school is trying to take an annual photo of all the students. The students are asked to stand
in a single file line in non-decreasing order by height. Let this ordering be represented by the
integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are
standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].'''

 
# Hint - Build the correct order of heights by sorting another array, then compare the two arrays.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        c = 0
        h = sorted(heights)
        for i in range(n):
            if heights[i] == h[i]:
                pass
            else:
                c += 1
        return c
             