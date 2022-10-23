'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
 such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead
 have the result be placed in the first part of the array nums. More formally, if there are
  k elements after removing the duplicates, then the first k elements of nums should hold the
   final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input
array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        l = len(nums)
        while fast<l:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] ,nums[fast] = nums[fast] ,nums[slow]
                fast += 1
        return slow+1

'''
slow pointer indicates the index where we had a duplicate value and fast 
pointer indicates the index of a non-duplicate value and we swap them both 
to not disturb the actual sequence of array.
we just have to return the index i+1 
from where all duplicate values will start occuring after we placed all non duplicate values in first i index
'''
