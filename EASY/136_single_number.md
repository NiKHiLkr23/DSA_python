### Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

### You must implement a solution with a linear runtime complexity and use only constant extra space.

## [136. LeetCode](https://leetcode.com/problems/single-number/)
#

## Approach 1
Using hash-map (python-dictionary).

We store the count of each element in dictionary and check for the eleemnt which appeared only one time.
```python
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key
```
#
## Approach 2
Using Bit-wise operator 

`^` 

(XOR)

```python
def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
```

```python
   # in-place solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
```    

#

## Approach 3
Hash-set of nums will give us all the values.

difference of 2*(Sum of hash-set) and sum of nums will give us the exact number that appeared just once.  

```python
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
```