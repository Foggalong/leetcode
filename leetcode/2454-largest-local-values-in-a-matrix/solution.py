class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Return a matrix of the largest values in every contiguous
        3 x 3 matrix in the input matrix `grid`.
        """

        # size of the maxLocal output matrix
        new_n = len(grid) - 2

        maxLocal = []
        for i in range(new_n):
            maxLocal.append([])
            for j in range(new_n):
                maxLocal[i].append(
                    max(max(grid[i+k][j:j+3]) for k in range(3))
                )

        return maxLocal
        
