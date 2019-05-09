"""
The mountain increases until it doesn't. The point at which it stops increasing is the peak.
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(0, len(A)):
            if A[i] > A[i+1]:
                return i

"""
One line solution
"""
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # A.index() gets an index and max(A) returns the highest value
        return A.index(max(A))
"""
Binary solution
"""
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low = 0
        high = len(A)-1
        while low < high:
            mid = (low + high)//2
            if A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid
        return high