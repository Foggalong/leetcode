# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode], parent=TreeNode()) -> int:
        """
        Given the root of a binary tree where each node as node.val coins,
        with the number of nodes being equal to the number of coins across
        the whole tree. Return the minimum number of moves required to get
        exactly one coin at every node, where a move is moving single coin
        from a parent to a child or vis versa.

        Note the function declaration is modified from the question to add
        the optional `parent` parameter. This is the root's parent, with a
        default value of an empty node. Including this makes the structure
        of the algorithm simpler, otherwise it we'd need a helper function
        so that the base case was handled.
        """

        # sum how many moves are needed for each child branch from root
        moves = 0
        for child in (root.left, root.right):
            # skip the cases where it doesn't exist
            if child is None: continue
            # recursively check child branches of the child branch
            moves += self.distributeCoins(child, root)

        # must keep 1 coin behind at each node. note that this number
        # could be negative if either root.val started on 0 (so needs
        # coins from its parent/child) or it became negative after it
        # sent coins to its children in the recurssive call above
        to_transfer = root.val - 1

        # move that many coins from the child to the parent
        parent.val += to_transfer
        # root.val -= to_transfer  # don't need this, done with root

        # return move tally after this, taking `abs` for negative case
        return moves + abs(to_transfer)

