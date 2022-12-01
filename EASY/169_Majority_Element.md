### Given an array nums of size n, return the majority element.
### The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### [Boyer-Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
### [Learn More about -> Majority vote algorithm](https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html)

## [169. LeetCode](https://leetcode.com/problems/majority-element/)
#

## Approach 1
Used a hash-map(python-dictionary) to store the count of elements.<br>
Return the element whose count is greater then `length_nums//2`

```python
class Solution:
    def majorityElement2(self, nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(nums)//2:
                return n

```
#

## Approach 2

Used a variable - `res`  to store the element if count==0.<br>
Increment count if the same value is seen else decrement. 

If count reaches zero again we assign the next element to *res*. 

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if count==0:
                res = i
            count += (1 if i==res else -1)
        return res
```
#

<h2>For certain edge case's where majority element is not present

For example:<br>
`list = [ 1,2,2,1,1,2]`</h2>

We find the majority element using [Boyer-Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) in a separate *funtion* <br>
And check if it is greater that `length_nums//2 `by looping thorugh the array `nums`.

```python
class Solution:
    def majorityElement(self, A, N):
        '''
        A = given_array 
        N = len(A)
        '''
        #Your code here
        def maj(A):
            res, count = 0,0
        
            for n in A:
                if count == 0:
                    res = n
                count += (1 if n==res else -1)
            return res
        r = maj(A)
        c=0
        for i in A:
            if i ==r:
                c += 1
        if c > N//2:
            return r
        else:
            return -1
```
<h2>

> Please refer to the aforementioned articles on *Majority Vote Algorithm* to have a better understanding.
</h2> 