# Given an integer, write a function to determine if it is a power of three.
# Example: Input: 27 => Output: true ; Example: Input: 45 => Output: false
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True

        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3

        return True
