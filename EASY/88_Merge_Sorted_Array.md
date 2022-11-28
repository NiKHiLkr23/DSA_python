<h3>You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.</h3>

## [88. LeetCode](https://leetcode.com/problems/merge-sorted-array/)

#

## Approach

<h3>
We iterate through each item in nums1 in reverse i.e; from the end, 
and verify if the element of nums1 is greater or lower then the value of nums2 ; until the len_nums2 is equal to zero.

If value_at_nums2 is greater we put it in the nums1
Else we put the last element that is m-1<sup>th</sup> at m+n-1<sup>th</sup> position in nums1.
</h3>



```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_nums1,len_nums2 = m-1, n-1
        iter = m + n-1
        while len_nums2 >= 0:
            if len_nums1 >= 0 and nums1[len_nums1] > nums2[len_nums2]:
                nums1[iter] = nums1[len_nums1]
                len_nums1 -= 1
            else:
                nums1[iter] = nums2[len_nums2]
                len_nums2 -= 1

            iter -= 1
```
#

### using built-in `sort()` function

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
```

