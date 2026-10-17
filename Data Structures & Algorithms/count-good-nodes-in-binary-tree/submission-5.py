# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        """
        DFS Depth First Search

        Make a function to be used to recursively iterate down

        Should have max value and root in its pass parameter

        When returning, should return current recursively called answer and add one if met condition
        
        If statement to compare the passsed in max value to current value

        If so then we will update max value and add 1

        This return is technically like a counter
        """
        return self.isGood(root,root.val)

    def isGood(self, root: TreeNode, maxval: int) -> int:
        good = 0

        if not root:
            return 0

        if maxval <= root.val:
            maxval = root.val
            good = 1

        return self.isGood(root.left, maxval) + self.isGood(root.right, maxval) + good
            
