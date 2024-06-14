class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Given an integer array `nums`, return the minimum number of entry
        increments to make every value in `nums` unique.
        """

        move_count: int = 0
        # nums can't contain negatives, so use -1 to identify the first value
        last_value: int = -1

        # iterate over index and values in nums in ascending order by value
        for i, n in sorted(zip(range(len(nums)), nums), key=lambda x: x[1]):
            # nought to do for smallest value except save it
            if last_value == -1: last_value = n; continue

            # current value could be smaller than last value if repeated entries
            if n <= last_value:
                # find and add incremenets necessary to make n unique
                to_add: int = last_value - n + 1
                nums[i] += to_add
                move_count += to_add

            # update last value
            last_value = nums[i]

        return move_count
