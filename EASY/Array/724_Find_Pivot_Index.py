'''Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of
the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there
are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1'''

# Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/


## Maths OP
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t_sum = sum(nums)
        sum_i = 0
        for i in range(len(nums)):
            if sum_i * 2 + nums[i] == t_sum:
                return i
            else:
                sum_i += nums[i]
        return -1

# using left-right as the question demands!

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for index,num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

