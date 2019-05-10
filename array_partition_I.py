"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible. 
"""

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    nums = sorted(nums)     # to make it as big as possible, array should be sorted
    result = 0      # sum will be stored here
    for i in range(0, len(nums) - 1, 2):        # iterate from first to second last counting every second element
      result += min(nums[i], nums[i+1])       # get min and add to the result

    return result

"""
Fast one line solution 
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])    