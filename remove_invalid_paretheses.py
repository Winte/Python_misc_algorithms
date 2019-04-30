class Solution(object):
    def removeInvalidParentheses(self, s):
        if not s:
            return [""]

        # Keeping track of the index we have seen and the index we removed
        # We never look back, but with recursive, the average time complexity should be O(n^2)
        def remove(s, last_iterate_index, last_remove_index, parents):
            # The moment balance < 0, the moment we find the first invalid paranthese
            balance = 0
            for i in range(last_iterate_index, len(s)):
                if s[i] == parents[0]:
                    balance += 1
                elif s[i] == parents[1]:
                    balance -= 1
                if balance >= 0:
                    continue

                # Now we find an invalid
                for j in range(last_remove_index, i + 1):
                    # We remove in either two condition:
                    # 1. j eqauls to last_remove_index --> which means the invalid paranthese is the first element of the string
                    # 2. remove the first invalid paranthese
                    if s[j] == parents[1] and (j == last_remove_index or s[j-1] != parents[1]):
                        # We only pass in the iterate and remove index with respect to the original string
                        remove(s[:j] + s[j+1:], i, j, parents)
                return

            # Should consider the reversed order
            # Remember to reverse parents also
            reversed_s = s[::-1]

            # Only after we consider the reversed order can we append to result array
            if parents[0] == '(':
                remove(reversed_s, 0, 0, parents[::-1])
            else:
                result.append(reversed_s)
        result = []
        remove(s, 0, 0, ['(', ')'])
        return result
