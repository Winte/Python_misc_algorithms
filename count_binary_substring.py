"""
Group By Character 
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively. 
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
      # An intuitive approach will be to group the binary string into chunks.
        chunks, consecutive, result = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        for i in range(1, len(chunks)):
            result += min(chunks[i], chunks[i - 1])
            # The answer will be simply to sum the min of length of neighboring chunks together.
        return result

"""
An alternative way is to find the positions where the bits flip and we can derive the chunks from the positions of the flips.
"""

class Solution:
    def countBinarySubstrings(self, s):
        flips, result = [0], 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                flips.append(i)
        flips.append(len(s))
        chunks = [a - b for (a, b) in zip(flips[1:], flips)]
        for i in range(1, len(chunks)):
            result += min(chunks[i], chunks[i - 1])
        return result

"""
In 3-lines
"""       
class Solution:
    def countBinarySubstrings(self, s):
        flips = [0] + [i for i in range(1, len(s)) if s[i] != s[i - 1]] + [len(s)]
        chunks = [a - b for (a, b) in zip(flips[1:], flips)]
        return sum(min(a, b) for a, b in zip(chunks, chunks[1:])) 

