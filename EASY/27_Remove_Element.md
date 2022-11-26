<h3>Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
 The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums
should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums. </h3>

## [27. LeetCode](https://leetcode.com/problems/remove-element/)

#

## *Approach* 

Slow pointer - Fast pointer
We iterate through the array using slow and fast pointer and whenever we find a value != val we swap it with the element the slow_index and increment the slow-pointer.

return the final position of slow-pointer
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return slow
```
#

## Approach-2

Exactly the same as above but with less readability.


```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for element in nums:
            if element != val:
                nums[k] = element
                k += 1
        return k
```
