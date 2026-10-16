# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maximum = 0

        def recursionInLeaf(root):
            nonlocal maximum
            
            if not root:
                return 0

            leftlength = recursionInLeaf(root.left)
            rightlength = recursionInLeaf(root.right)

            maximum = max(maximum, leftlength + rightlength)

            return max(leftlength, rightlength) + 1

        recursionInLeaf(root)
        
        return maximum
