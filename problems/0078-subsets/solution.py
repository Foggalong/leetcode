from itertools import chain, combinations
import numpy as np

"""
It was odd that this problem came up today, because I used the powerset
recipe from the itertools module to do yesterday's Daily LeetCode. This
is included as `powerset` below. Today's solution was also started at a
time long past, so I finished that rather than starting anew. It is for
sure not the best way to do this.

EDIT (May 23rd) also added an implementation of the binary filtering I
saw someone discuss in the comments because it piqued my interest.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """List all subserts using binary filtering"""

        n: int = len(nums)

        # start with the base case, the emptyset and itself
        powerset: List[List[int]] = [[], nums]
        if n == 1: return powerset

        # only interested in non-empty subsets, so start at 1
        for i in range(1, 2**n - 1):
            # convert i to an n-bit binary string
            binary: str = f"{i:b}".zfill(n)
            # use this binary string to filter nums to a subset
            powerset.append([nums[j] for j in range(n) if binary[j] == '1'])

        return powerset        


    def subsetsBad(self, nums: List[int]) -> List[List[int]]:
        """List all subserts using recurrsive function"""

        n: int = len(nums)

        # start with the base case, the emptyset and itself
        powerset: List[List[int]] = [[], nums]
        if n == 1: return powerset

        # top level iteration over the elements in nums
        for i in range(n):
            # add set with the ith element removed
            iless_nums: List[int] = nums[:i] + nums[i+1:]
            powerset.append(iless_nums)
            # now consider the subsets of this set
            for iless_subset in self.subsets(iless_nums):
                # add any newly found subsets
                if iless_subset not in powerset:
                    powerset.append(iless_subset)

        return powerset


    def powerset(self, nums: Iterable[int]):
        """
        Return the power set of an iterable, excluding the empty set. Example:
        powerset([1,2,3]) → (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
        """
        # starting the range from 1, not 0, skips the emptyset
        return chain.from_iterable(combinations(nums, r) for r in range(1, len(nums)+1))

