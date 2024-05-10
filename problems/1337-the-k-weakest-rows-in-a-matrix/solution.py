# in Python 3.6 or earlier, standard dicts aren't ordered 
from collections import OrderedDict

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Takes a binary matrix (mat) and an integer (k) as inputs,
        where the rows of mat are sorted descending. Returns the
        indices of the k rows with the smallest row sums, using
        the row index as a tie breaker (with the lowest winning).
        """

        m = len(mat)     # number of rows
        n = len(mat[0])  # number of columns

        # create dictionary of row sums
        row_sums = OrderedDict([(i, 0) for i in range(m)])

        # sum each row, halting a row when a zero is found
        for row_index in range(m):
            for col_index in range(n):
                if mat[row_index][col_index] == 0:
                    # all future values also 0 since sorted 
                    break
                else:
                    row_sums[row_index] += 1

        # sort dictionary by descending order of value
        row_sums = OrderedDict([
            (r, v) for r, v in sorted(row_sums.items(),
                                      key=lambda item: item[1])
        ])

        # return first k keys 
        return list(row_sums.keys())[0:k]