"""
Transpose Matrix

Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Ex:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

"""


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)       # number of rows
        columns = len(A[0])     # number of columns
        temporary = []
        res = []
        for i in range(columns):
            for j in range(rows):
                # the algorithm goes as follow: A[0][0], A[1][0], A[2][0], A[0][1], A[1][1] etc
                temporary.append(A[j][i])
            res.append(temporary)        # add every row
            temporary = []      # clear temp list so it can be used again

        return res
