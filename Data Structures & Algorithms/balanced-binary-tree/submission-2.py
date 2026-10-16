# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.lengthOfBranch(root)
        return self.balanced

    def lengthOfBranch(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lengthleft = self.lengthOfBranch(root.left)
        lengthright = self.lengthOfBranch(root.right)

        if abs(lengthleft - lengthright) > 1:
            self.balanced = False
        
        return max(lengthleft, lengthright) + 1

