"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
Ex:
Input: [4,2,5,7]
Output: [4,5,2,7]
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = [x for x in A if x % 2 != 0]      # separate odd numbers
        even = [x for x in A if x % 2 == 0]     # separate even numbers

        result = []

        for x, y in zip(even, odd):
            result.append(x)
            # join even and odd numbers starting from even
            result.append(y)

        return result

# Two pointer solution


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1
        even = 0
        size = len(A)

        while odd < size and even < size:
            while odd < size and A[odd] % 2 == 1:  
                odd += 2
            while even < size and A[even] % 2 == 0:  
                even += 2
            if odd < size and even < size:
                A[odd], A[even] = A[even], A[odd]
                odd += 2
                even += 2

        return A
