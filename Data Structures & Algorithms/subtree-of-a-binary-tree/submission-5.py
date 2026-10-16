# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same = False
        
        if not root:
            return False

        if root.val == subRoot.val:
            same = self.isSame(root, subRoot)
        
        leftMain = self.isSubtree(root.left, subRoot)
        rightMain = self.isSubtree(root.right, subRoot)

        return leftMain or rightMain or same
        


    def isSame(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True

        elif not root or not subRoot:
            return False

        else:
            if root.val != subRoot.val:
                return False

            leftSub = self.isSame(root.left, subRoot.left)
            rightSub = self.isSame(root.right, subRoot.right)

            return leftSub and rightSub

        
