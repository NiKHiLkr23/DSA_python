## Given two binary strings a and b, return their sum as a binary string.
<h3>
Example 1:

Input: a = "11", b = "1"

Output: "100"
</h3>

## [67. LeetCode](https://leetcode.com/problems/add-binary/)

#
## Approach
Let's understand binary addition :
Similar to decimal addition where the range is 0-9 and if the value gets beyond 9 we have a carry...<br>
In binary the range is 0-1 which implies if the result is more than one we have a carry else no-carry.<br>
So, 
`1+1 = 2` which is more than one so we'll have a `carry = 1` and the result is `zero`..<br>
The process follows until we have a zero or the number ends and the carry `1` will be returned as it is.

<h2> 
carry = 0 <br>
sum = carry+c1+c2 <br>
Thus, sum =2 <br>
and, carry = 1 <br>
result = 0
</h2>

>I hope you got the point!


```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a,b = a[::-1],b[::-1]

        for i in range(max(len(a),len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) -ord("0") if i < len(b) else 0

            total =digitA + digitB + carry
            char = str(total%2)
            res = char + res
            carry =  total//2
        if carry:
            res = "1" + res
        return res
```
#

## Self Explanatory

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry %2)
            carry //= 2
        return result[::-1]
```