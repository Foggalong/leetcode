class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.
        """

        # starting values
        min_i: int = 0               # smallest row index 
        min_j: int = 0               # smallest col index
        max_i: int = len(matrix)     # largest row index
        max_j: int = len(matrix[0])  # largest col index (guaranteed at least one)

        elements = []

        while True:
            # add top most unexplored row using splicing
            elements += matrix[min_i][min_j:max_j]
            min_i += 1  # row explored, never return here
            if min_i == max_i: break

            # add right most unexplored col using loop (due to list-of-list structure)
            elements += [matrix[i][max_j-1] for i in range(min_i, max_i)]
            max_j -= 1  # column explored, never return here
            if min_j == max_j: break

            # add bottom most unexplored row using splicing
            elements += matrix[max_i-1][min_j:max_j][::-1]  # BUG can't be integrated?
            max_i -= 1  # row explored, never return here
            if min_i == max_i: break

            # add left most unexplored col using loop
            elements += [matrix[i][min_j] for i in range(max_i-1, min_i-1, -1)]
            min_j += 1  # first column explored
            if min_j == max_j: break

        return elements
