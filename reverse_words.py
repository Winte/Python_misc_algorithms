"""
Reverse Words in a String

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take Code contest"
Output: "s'teL ekat edoC tsetnoc"

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')        # creates a list of words
        reverse = []        # reversed words will be stored here
        for word in s:
            # adds reversed word to the reverse list
            reverse.append(word[::-1])

        res = ' '.join(reverse)      # joins words with a space

        return res
