<h3>Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
 such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead
 have the result be placed in the first part of the array nums. More formally, if there are
  k elements after removing the duplicates, then the first k elements of nums should hold the
   final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.</h3>

> Do not allocate extra space for another array. You must do this by modifying the input
array in-place with O(1) extra memory.

## [26. LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

#

## *Approach*
we iterate through the array using a slow pointer and a fast pointer.
fast pointer searches for the duplicates and if found we increment the fast pointer and look if the next element is also a duplicate or not, if not then we increment the slow pointer and swap the elements.
`retrun (slow_pointer_index + 1)`


```python
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
```

If you're unable to understand please debug this code to have a better understanding!



