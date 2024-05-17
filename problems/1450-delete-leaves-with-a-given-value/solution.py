# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Given a binary tree `root` and an integer `target`, delete all the leaf nodes with
        value `target`. It does this by recursively examining the left and right branches,
        pruning any target leaves as necessary.
        """

        # cases where branch empty or is just the target leaf
        if (root is None) or self.isTargetLeaf(root, target): return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # if the root has become a target leaf, prune and finish
        if self.isTargetLeaf(root, target): return None

        return root


    def isTargetLeaf(self, root: Optional[TreeNode], target: int) -> bool:
        """
        Boolean helper function to check whether the current root is a leaf node (A) and
        has the desired target value (B). Utilises the fact that "not(not A or not B)"
        will evaluate quicker than "A and B" due to possible early exit within OR, while
        still being a logically equivalent statement. 
        """

        return not ((root.left is not None) or (root.right is not None) or (root.val != target))

