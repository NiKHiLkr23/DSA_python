<h3>You are given a large integer represented as an integer array digits, where each digits[i] is
 the ith digit of the integer. The digits are ordered from most significant to least significant in
  left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.</h3>

## [66. LeetCode](https://leetcode.com/problems/plus-one/)

#
### Pythonic Solution

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, str(int(''.join(map(str, digits)))+1))
```
#

## Approach
<h3>We're given a list of digits, and the idea here is to convert that list to an integer, num. So each digit is multiplied by the proper place value and added to num. For example, if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3, so this results in 3000, which is added to num. Then 8 is multiplied by 10^2 and added to num, and so on.

The last step is to add 1 to num, convert it to a list and return that list.</h3>
```python
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]
```
#

### Easy to understand solution

we start from the last element of the list and check if it is equal to 9 , if it is we make it zero and check the second-last element , if second-last element is not equal to 9 we add 1 to the second last element.
In this way we check for consecutive 9's from the end if not found we move out of the while-loop and perform the required operation.

we return the modified result-list.

```python
def plusOne(self, digits):
        length = len(digits) - 1
        res = list(digits)
        while res[length] == 9:
            res[length] = 0
            length -= 1
        if (length < 0):
            res = [1] + res
        else:
            res[length] += 1
        return res
```