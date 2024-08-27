from itertools import chain, combinations

# This will be far from the most efficient solution because it requires
# enumerating and then XORing every possible subset separately. Knowing
# LeetCode, there is probably some shortcut here I just don't have the
# time to go looking for it today. 

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Given an array nums, return the sum of all XOR totals for every subset
        of nums, where the XOR total is defined as the bitwise XOR of all its
        elements, or 0 if the array is empty.
        """
        xor_sum = 0
        for subset in self.powerset(nums):
            ss_sum = subset[0]
            for x in subset[1:]:
                ss_sum ^= x
            xor_sum += ss_sum
        return xor_sum

    def powerset(self, nums: Iterable[int]):
        """
        Return the power set of an iterable, excluding the empty set. Example:
        powerset([1,2,3]) → (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
        """
        # starting the range from 1, not 0, skips the emptyset
        return chain.from_iterable(combinations(nums, r) for r in range(1, len(nums)+1))
