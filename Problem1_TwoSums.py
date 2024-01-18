"""
1. Two Sum
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    """ Take a list of integers, return a list of indices
    within the list of integers where the numbers sum equals
    the target.
    """
    indices = [0,0]
    # iterate over the list of numbers
    for i in range(len(nums)):
        #trim down the work by scanning the remaining list
        #for the value that is target - current iterable
        secondNum = target - nums[i]
        #chance to throw exception if value above isnt found in list
        try:
            #if number is in the list great, if not move on
            if nums.index(secondNum) == i:
                continue
            else:
                indices = [i, nums.index(secondNum)]
                return indices
        except:
            continue

