class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Given an integer rowIndex, return the rowIndexth (0-indexed) row of
        the Pascal's triangle as a list of integers.
        """

        # catch degenerate case
        if rowIndex == 0: return [1]

        lastRow = []
        for rowNum in range(0, rowIndex):  
            # row's internal values are pair-sums of the previous row
            lastRow = [sum(lastRow[i:i+2]) for i in range(rowNum)]
            # row's first and last values are both '1'
            lastRow = [1] + lastRow + [1]

        return lastRow
