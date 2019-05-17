"""
Smallest Range I

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have an array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
Ex:
Input: A = [0,10], K = 2
Array B = [2,8]
Output: 6

"""

class Solution:
  def smallestRangeI(self, A: List[int], K: int) -> int:
    smallest = min(A)       # smallest value
    biggest = max(A)        # biggest value
    difference = abs(biggest - smallest)        # absolute value of difference

    if difference <= 2*K:   return 0        # you can add up to K and substract up to K, so all digits will be equal

    else:   return difference - 2*K     # when difference is bigger, you can dicrease it by adding K to smallest and substructing K from biggest


# Or 

class Solution:
  def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        return max(A) - min(A) - 2*K if max(A) - min(A) - 2*K > 0 else 0 