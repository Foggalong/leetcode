class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        twoSum takes a list of integers (nums) and an integer
        (target) as inputs and then returns then returns [i,j]
        where nums[i] + nums[j] == target. It is assumed that
        such a pair of indexes exist and that nums is at least
        two items long.
        """

        # create a location map, O(n)
        locations = {nums[i]: i for i in range(len(nums))}

        # iteracte over values, O(n)
        for i in range(len(nums)):
            try:
                # compute nums[j] = target - nums[i] and then
                # try to access j from the location map 
                j = locations[target - nums[i]]
                # can't reuse values
                if j == i: continue
                # if error wasn't thrown, done!
                return [i, j]
            # if nums[j] not in nums, KeyError will be thrown
            except KeyError:
                continue

