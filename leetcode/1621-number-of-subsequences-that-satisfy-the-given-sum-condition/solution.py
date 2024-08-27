class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Returns the number of non-empty subsequences of nums such
        that the sum of the minimum and maximum element is less or
        equal to target. Since the answer may be too large, it is
        returned modulo 10^9 + 7.
        """

        count = 0
        mod   = 10**9 + 7

        # more efficient to sort the full list than to find
        # the minimum and maximum of all the subsequences
        nums.sort()
        # iterate over subsequence starting position in
        # ascending order, and within that over length of
        # subsequence in descending order
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] + nums[j] <= target:
                # sequence of length n has 2^n subsequences
                count += pow(2, j-i, mod)
                # don't double count substrings 
                i += 1
            else:
                j -= 1

        return count % mod
