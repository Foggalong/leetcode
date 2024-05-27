class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        An array of non-negative integers `nums` is considered special
        if there exists an `x` such that there are exactly `x` numbers
        in `nums` that are greater than or equal to `x`. Returns `x` if
        the input is special, else returns -1. Note that if it exists,
        `x` is unique.
        """

        for x in range(len(nums)+1):
            if x == sum(True if n >= x else False for n in nums):
                return x
        return -1
