class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """
        Return the maximum possible sum of a tree's node values after performing XOR
        on any two adjacent nodes any number of times. Note that (A XOR k) XOR k = A,
        and our tree is connected, so we can equivalently consider just any two nodes
        rather than adjacent nodes specifically. This is because we can simply apply
        A XOR k twice on the intermediate nodes to no effect. This makes the `edges`
        argument here entirely redundant which was a weird choice by LeetCode.
        """

        # store a list of by how much each value would change after after XOR'd
        xor_impact: Tuple[int] = ((value^k) - value for value in nums)

        # sum of all node values can serve as our base case
        node_sum: int = sum(nums)

        # we'll iterate over these differences in descending order
        xor_impact: iterable[int] = iter(sorted(xor_impact, reverse=True))
        for value in xor_impact:
            # calculate impact if we XOR this node and the next. giving
            # next default of -value handles case where there's an odd
            # number of nodes, and it would be beneficial to XOR the last
            # node but we can't because there's no other to XOR alongside
            paired_xor_impact: int = value + next(xor_impact, -value)
            # if beneficial, add pairs' impact and move to next pair
            if paired_xor_impact > 0: node_sum += paired_xor_impact
            # if no further improvement, must be done since descending
            else: break
        
        return node_sum

        
