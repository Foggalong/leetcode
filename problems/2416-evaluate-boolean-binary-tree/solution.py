# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        Recursively evaluate a boolean binary tree. Leafs nodes
        have 0 representing false and 1 representing true, while
        non-leaf nodes have 2 representing OR and 3 representing
        AND. Output will be a single boolean value.
        """

        # If a node is AND, we can return false early if either
        # branch evaluates to false, else return true. This may
        # save us evaluating half of the subsequent nodes.
        if root.val is 3:
            if not self.evaluateTree(root.left): return False
            if not self.evaluateTree(root.right): return False
            return True
        
        # If a node is OR, we can return true early if either
        # branch evaluates to true, else return false. This may
        # save us evaluating half of the subsequent nodes.
        if root.val is 2:
            if self.evaluateTree(root.left): return True
            if self.evaluateTree(root.right): return True
            return False

        # If node isn't OR or AND, we must be at a leaf so just
        # want to return the value of the node
        return root.val
