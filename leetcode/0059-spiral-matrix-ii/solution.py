class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.
        Note this works very similar to my solution to #54 (Spiral Matrix I) but
        ommits the now-unnecessary checks for break conditions. This could be made
        more efficient by condensing the case for each direction using, but felt
        like that would be more trouble than it was worth.
        """

        min_i: int = 0  # smallest row index 
        min_j: int = 0  # smallest col index
        max_i: int = n  # largest row index
        max_j: int = n  # largest col index

        # preallocate an n by n matrix of zeros
        matrix: List[List[int]] = [[0]*n for _ in range(n)]

        element: int = 1
        while element <= n*n:
            # add top most unfilled row
            for j in range(min_j, max_j):
                matrix[min_i][j] = element
                element += 1
            min_i += 1  # row filled, never return here

            # add right most unfilled column
            for i in range(min_i, max_i):
                matrix[i][max_j-1] = element
                element += 1
            max_j -= 1  # column filled, never return here

            # add bottom most unfilled row
            for j in range(max_j-1, min_j-1, -1):
                matrix[max_i-1][j] = element
                element += 1
            max_i -= 1  # row filled, never return here

            # add left most unfilled column
            for i in range(max_i-1, min_i-1, -1):
                matrix[i][min_j] = element
                element += 1
            min_j += 1  # column filled, never return here

        return matrix
