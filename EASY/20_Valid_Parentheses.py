'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #run through each Parentheses
        for i in s:
            #Check if it opening Parentheses then push it into stack
            if i=='(' or i =='[' or i=='{':
                stack.append(i)
            #If it closing Parentheses then check length of stack is greater than 0 or not
            elif(len(stack)):                
                #pop the last element
                el = stack.pop()
                #if element is not opposite of popped element than return false
                if el=='(' and i !=')':
                    return False
                elif el=='[' and i !=']':
                    return False
                elif el=='{' and i !='}':
                    return False
            #If above 2 condition fails return false
            else:
                return False
        #if there is any Parentheses in stack return false
        if(len(stack)):
            return False
        #otherwise return true
        else:
            return True


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = { ')':'(' ,']': '[' , '}':'{' }

        for char in s:
            if char in d:
                if stack and stack[-1] == d[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
         
        return True if not stack else False