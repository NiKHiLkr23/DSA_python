'''A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B
 are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way
 to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
 where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
'''


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        temp=""
        arr=[]
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                stack.pop()
            
            temp += i
            
            if len(stack)==0:
                temp = temp[1:-1]
                arr.append(temp)
                temp =""
        return "".join(arr)


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
      
        stack = []
        n =len(S)
        sh=[False]*n

        for i,op in enumerate(S):
            if op =='(':
                stack.append(i)
            else:
                old_i = stack.pop()

                if len(stack)>0:
                    sh[i] = True
                    sh[old_i] = True
        res = ""
        for i,op in enumerate(sh):
            if op:
                res += S[i]
        return res