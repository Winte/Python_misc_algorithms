"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

* Also, a self-dividing number is not allowed to contain the digit zero. 
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []     # results will be stored in this list
        for i in range(left, right + 1):        # I will represent all prospects
            count = 0
            # turning int into string to be able to get all digits
            string_num = str(i)
            length = len(string_num)
            for digit in string_num:
                # digit can't be zero and number has to be divided by digit
                if int(digit) == 0 or i % int(digit) != 0:

                    # abandon particular number when conditions are met (break for digit loop and get next i)
                    break

            else:
                count == length
                # when count equals length so all digits where checked, add number to result list
                result.append(i)

        return result
