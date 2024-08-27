class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Given an integer matrix mat as input, return the sum
        of all the entries on the diagonal and anti-diagonal
        """

        # running total
        total = 0
        # square matrix so m == n
        n = len(mat)
        for i in range(n):
            # in ith row add ith and (n-i)th entry to total
            total += mat[i][i] + mat[i][n-i-1]
        # avoid double counting middle element if n odd
        if n % 2: total -= mat[int(n/2)][int(n/2)]

        return total

