"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            # to be able to slice results[-2:], start should be at F(2)
            return 1

        results = [0, 1]        # at this point N = 2 or higher

        for i in range(1, N):
            # add sum of last 2 numbers to results {fib(n-1) + fib(n-2)}
            results.append(sum(results[-2:]))

        return results[-1]      # return last result from the list
