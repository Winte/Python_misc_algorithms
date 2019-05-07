"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        # Numbers that are needed to meet the target will be stored here along with an index    
        wanted_nums = {}
        # Interating through numbers list
        for i in range(len(nums)):
            # If number in wanted_nums it means we've got the sum!
            if nums[i] in wanted_nums:
                return [wanted_nums[nums[i]], i]
            # If not....
            else:
                wanted_nums[target - nums[i]] = i


