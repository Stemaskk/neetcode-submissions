# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:
            """
            if root.val == p and root.right == q:
                return root
            elif root.val == q and root.left == p:
                return root
            elif root.left == p and root.right == q:
                return root
            else:
                if root.left.val <= q.val and root.left.val >= p.val:
                    root = root.left
                else:
                    root = root.right

            """

            if root.val >= min(p.val, q.val) and root.val <= max(q.val, p.val):
                return root
            elif q.val < root.val:
                root = root.left
            else:
                root = root.right
        