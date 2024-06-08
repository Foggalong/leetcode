class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return true if
        there's a contiguous subarray of nums of at least length two
        whos elements sum to a multiple of k. Return false otherwise.
        """

        # skip degenerate cases
        if len(nums) < 2: return False

        # will track entry sums mod k of subarrays of increasing length
        # starting from the first element. if when iterating we find a
        # total which we've found previously, that must mean this subarray
        # itself has a subarray which sums to 0 mod k 
        prev_totals: set = set()

        # neat idea from @piossel to store the previous iteration
        # and delay adding as a way of accounting for len >= 2
        last_total: int = 0

        # running entry sums mod k (initial applies it to nums[:0] ...)
        subsums = accumulate(nums, lambda x, y: (x + y) % k, initial=0)
        next(subsums)  # (...but adds an extra 0 we then must skip) 

        for total in subsums:
            # only need to find one good subarray
            if total in prev_totals: return True

            prev_totals.add(last_total)
            last_total: int = total

        return False 


    def checkSubarraySumSlow(self, nums: List[int], k: int) -> bool:
        """
        First attempt that tried to do this by exhaustion; almost got
        there but runs out of time on a few of the longer test cases.
        """

        # iterate over starting points for the subarray
        for start in range(0, len(nums)-1):
            # subarray must include at least two elements 
            subarray_total = nums[start]
            end = start + 1

            while end < len(nums):
                # add new element to end of subarray
                subarray_total += nums[end]
                end += 1

                # only need to find one good subarray
                if not subarray_total % k: return True

        return False                
        
