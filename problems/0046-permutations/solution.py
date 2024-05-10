class Solution:
    """
    Given an array nums of distinct integers, return all the
    possible permutations of nums (given in any order).
    """

    def permuteItertools(self, nums: List[int]) -> List[List[int]]:
        """List all permutations using standard library""" 
        return [list(p) for p in itertools.permutations(nums)]

    def permute(self, nums: List[int]) -> List[List[int]]:
        """List all permutation using recurrsive function"""

        # need to put nums in list else will return as int
        if len(nums) == 1: return [nums]

        outputs = []
        # top level iteration over the elements in nums
        for i in range(len(nums)):
            # iterate over permutations of remaining entries
            for permutation in self.permute(nums[:i] + nums[i+1:]):
                # add first element to permutation of remaining
                outputs.append(nums[i:i+1] + permutation)

        return outputs

