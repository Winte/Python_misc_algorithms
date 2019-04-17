
def maxSubArray(self, nums):
    if not nums:
        return 0

    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        # No max subarray will include a negative sum prefix, because 
        # could have greater sum if just leave prefix off.
        # So if the current number is greater than the previous sum plus the
        # current number, don't include the previous sum / start over.
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)

return max_sum
       