"""
 Sort Array By Parity: Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
 Ex:
Input: [3,1,2,4]
Output: [2,4,3,1]
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for number in A:
            if number % 2 == 0:         # if remainder is equal 0, the number is even
                even.append(number)     # add to even
            else:
                # when remainder isn't equal 0, it's odd so add to odd
                odd.append(number)

        return even + odd
