## Write a function to find the longest common prefix string amongst an array of strings.
## If there is no common prefix, return an empty string
## [14. Leetcode](https://leetcode.com/problems/longest-common-prefix/)
#

###  Vertical Scanning *approach* -<br>
iterate through each word in strs-List one by one and compare the charaters starting from 0<sup>th</sup> index to i<sup>th</sup> index simultaneously for each word.<br>
Terminate in case any if the i<sup>th</sup> index charaters doesn't match.


  
**Time O(M)**  **Space O(1)**     
> worst-case all the strings in strs-List are same 

*M is the sum of all the characters in all strings in strs-List.*
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if (i == len(strs[j]) or strs[j][i] != c):
                    return strs[0][0:i];             
        return strs[0]
```              
Haven't initailized any result string to store the result *since* <br>
string concatenation = linear-time<br>
`string += c` -> *linear*
>it doesn't simply add one string at the end of another<br>
> it creates a new string