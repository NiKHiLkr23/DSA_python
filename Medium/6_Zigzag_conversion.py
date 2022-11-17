'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

class Solution:
    def convert(self, S: str, R: int) -> str:
        if R == 1 or R > len(S):  # corner case
            return S
        res, i, step = ['' for r in range(R)], 0, 0  # a string for each line
        for s in S:
            res[i] += s
            if i == 0:  # first row
                step = 1  # down
            if i == R - 1:  # last row
                step = -1  # up
            i += step
        return "".join(res)


# using the above solution will impact the overall time complexity; since -> string concatenation - Big O(length of string) 
# this can be reduced via the below method -> using list

# if len(s) <= numRows or numRows == 1:
# return s
# L = []
# for i in range(numRows):
# L.append([])

# index = 0
# for ch in s:
#      L[index].append(ch)
#      if index == 0:
#          step = 1
#      if index == numRows - 1:
#          step = -1
#      index += step
        
# return ''.join([''.join(item) for item in L])



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s 
        res =[]
        for r in range(numRows):
            increment = 2 * (numRows-1)
            for i in range(r,len(s),increment):
                res.append(s[i])
                if (r>0 and r<numRows-1 and
                 i + increment - 2 * r  < len(s) ) :
                    res.append(s[i+increment-2*r])
        return ''.join(res)