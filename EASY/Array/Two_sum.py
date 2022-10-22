
from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

''' the avobe solution has time complexity O(n^2) which is quite bad
Here, two nested loops are used where the outer loop iterates over all the elements of the
list and the inner loop iterates from current index of the outer loop up to the end of list '''


class solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx

# This solution is way better than previous one `cause we iterate over the list of number just once
# Hence, making the the complexity O(n)
# Here, we take advantage of the python dictionary and create an Empty dictionary to
# store the value adn index of each list element as key-pair respectively  
""" then we iterate through the indices and values of the list containing our numbers. If the 
    difference between the target and the current value in the list is already included ad a key in the 
    dictionary, it implies that the current value and the value stored in the dictionary is the
    solution to our problem.
    Else we simply add the value and index as a key-value pair in our dictionary and keep iterating
    until we find the solution"""




# if __name__ == '__main__':
#     list = [ 2, 4, 5, 6, 7, 21, 4 ,6 ]
#     s = solution()
#     S = solution()

#     sol = solution.twoSum("",list, 12)
#     Sol = Solution.twoSum("",list, 28)

#     print(sol)
#     print(Sol)
