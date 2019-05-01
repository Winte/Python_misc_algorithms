"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. The solution set must not contain duplicate triplets.

The key idea is only using dictionary to store occurrences.
"""

class Solution(object):
    def threeSum(self, nums):
        # Key: elements in nums
        # Val: number of occurrences
        # Can use defaultdict to make this shorter, but I don't want to use additional library
        lookup = dict()
        for num in nums:
            if not num in lookup:
                lookup[num] = 0
            lookup[num] += 1
        
        #Check 0, 0, 0 condition
        if 0 in lookup and lookup[0] > 2:
            res = [[0,0,0]]
        else:
            res = []
        
        #We will iterate by positive and then negative
        pos = [p for p in lookup if p > 0]
        neg = [n for n in lookup if n < 0]
        
        # check whether the missing value is in dictionary
        for p in pos:
            for n in neg:
                i = -p-n
                if i not in lookup:
                    continue
                # We now found possible correspondence in dictionary, but still little to compare
                # 1. the missing value is 0
                if i == 0 and lookup[i] > 0:
                    res.append([n, 0, p])
                # 2. the missing value is same as positive value, so the occurrences should be greater than 1
                elif i == p and lookup[i] > 1:
                    res.append([n, p, p])
                # 3. Same above
                elif i == n and lookup[i] > 1:
                    res.append([n, n, p])
                # 4. Deciding position in the answer
                elif i > p:
                    res.append([n, p, i])
                elif i < n:
                    res.append([i, n, p])
                
                # At here, we don't consider n < i < p, because we iterate through every possible pair in the for loops
                # So this situation (n < i < p)  will definitely be considered in other situation, in terms of i=p, p=i, or n=i, i=n
                # If you are still afraid, you can add the append code here and take set operation when returning answer


                    
        return res



