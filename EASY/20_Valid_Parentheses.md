<h3>Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. </h3>
## [20. LeetCode](https://leetcode.com/problems/valid-parentheses/)

# 

## *Approach 1*

We iterate through the given string of parentheses and each time a open parenthesis is encountereed we push it to the stack, but if it is a closed parentheses, we check if it matches with the parentheses-type at the top of the stack and pop it.
If stack is empty at the end we `return True`

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #iterate through each Parentheses
        for i in s:
            #Check if it is opening Parentheses then push it into stack
            if i=='(' or i =='[' or i=='{':
                stack.append(i)
            #If it is closing Parentheses then check length of stack is greater than 0 or not
            elif(len(stack)):                
                #if len(stack) > 0 -> pop the last element
                elment_at_top = stack.pop()
                #if element is not opposite of popped element than return false
                if elment_at_top=='(' and i !=')':
                    return False
                elif elment_at_top=='[' and i !=']':
                    return False
                elif elment_at_top=='{' and i !='}':
                    return False
            #If above 2 condition fails return false
            else:
                return False
        #if there is any Parentheses in stack return false
        if(len(stack)):
            return False
        #else return true
        else:
            return True
```
#

## *Aproach 2*
Using stack and Hashmap(Dict) instead of of `if-else` statements.<br>
Every time we encounter a closing bracket we check if it matches with the top of the stack and poop it.<br>
`return True` if stack is empty at the end


```python
    class Solution:
        def isValid(self, s: str) -> bool:
            stack = []
            d = { 
                ')':'(' 
                ,']': '[' ,
             '}':'{' }

            for char in s:
                if char in d:
                    if stack and stack[-1] == d[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)

            return True if not stack else False
```        