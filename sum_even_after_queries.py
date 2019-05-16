"""
Sum of Even Numbers After Queries
We have an array A of integers, and an array queries of queries.
Ex:
Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
"""


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even_sums = []      # sums will be stored here
        for query in queries:       # loop over queries
            A[query[1]] += query[0]     # required change
            # creates a list of even numbers - list comprehension
            even = [x for x in A if x % 2 == 0]
            even_sums.append(sum(even))     # add sum to the list of sums

        return even_sums

#    Harder but clever solution -   This way to calculate the sum it's not necessary to iterate over the list all the time. It's enough to just correct previous result according to the new number.


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        # sum of even numbers is calculated only once!
        even_sum = sum(x for x in A if x % 2 == 0)
        even_sums = []

        for x, k in queries:
            if A[k] % 2 == 0:
                # to keep the sum right - old value has to be subtract and new value added which gives the difference
                even_sum -= A[k]
            A[k] += x     # required change comes here
            if A[k] % 2 == 0:
                # here value is added to achieve the difference
                even_sum += A[k]
            # when the difference is achieved just add total sum to the list
            even_sums.append(even_sum)

        return even_sums        # return the result after the loop
