class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Given an integer numRows, returns the first numRows of Pascal's
        triangle as a list of lists if integers.
        """

        outRows = [[1]]  # preallocation catches numRows == 1 case
        lastRow = []

        # question indexes from 1, not 0, so must adjust
        for rowNum in range(1, numRows):  
            # row's internal values are pair-sums of the previous row
            lastRow = [sum(lastRow[i:i+2]) for i in range(len(lastRow)-1)]
            # row's first and last values are both '1'
            lastRow = [1] + lastRow + [1]
            outRows.append(lastRow)

        return outRows

