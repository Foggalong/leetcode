class Solution:
    """
    Observe that the optimal strategy is always to flip each row
    such that the leading digit is a one, then each column after
    the first to maximize the number of ones in that column. The
    score can then be computed without carrying out column flips
    explicitly, instead adding the highest possible contribution
    from each column.
    """

    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        Given an m x n binary matrix grid, carry out a series
        of row and column bit-flips to maximise the sum when
        each row is interpreted as a binary number, and then
        return that sum.
        """

        # define to avoid repeated `len` calls
        m = len(grid)
        n = len(grid[0])  # guaranteed at least one row

        # make each row's leading digit a one
        for i in range(m):
            if grid[i][0] == 0:
                # `1-entry` is equivalent to a bit-flip
                grid[i] = [1 - entry for entry in grid[i]]

        # sum maximum possible column contributions
        score = m*2**(n-1)  # first col is all 1s
        for j in range(1,n):
            # decimal value of binary one in jth column
            x = 2**(n-j-1)
            # multiplies x by number of ones in column j
            ones_sum = sum(x for i in range(m) if grid[i][j])
            # use partition to avoid looping over rows again
            zero_sum = m*x - ones_sum
            # want the largest of two possible contributions
            score += max(ones_sum, zero_sum)

        return score
