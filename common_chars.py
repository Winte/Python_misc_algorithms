"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
Ex:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        results = []
        i = 0
        # length of the first word will be decreasing so while is better than for
        while i <= len(A[0]) - 1:
            # because while checks the condition after every loop
            if all(A[0][i] in item for item in A):      # check if char occures in every word
                results.append(A[0][i])         # if yes, add to results list
                # return A list with words without first occurence of char
                A = [item.replace(A[0][i], '', 1) for item in A]
                i -= 1      # in case of deleting a char, deduct 1 to stay at the same index - 1 will be added in the next step
            i += 1

        return results
