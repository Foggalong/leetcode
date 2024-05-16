class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # handle degenerate case without work needed
        if numRows == 1: return s

        # initialise zigzag structure as list of lists
        zigzag: List[List[str]] = [[] for _ in range(numRows)]

        row = 0   # row index appending to
        inc = +1  # positive = down, negative = up

        for char in s:
            # add character to zigzag and advance string
            zigzag[row].append(char)
            row += inc

            # if reached boundary, change direction
            if (row == 0) or (row == numRows - 1):
                inc = -inc

        # concatenate a list of lists of characters
        return "".join(["".join(l) for l in zigzag])

