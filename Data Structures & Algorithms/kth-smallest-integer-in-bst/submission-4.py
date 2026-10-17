# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def DFS(root):
            if not root:
                return

            DFS(root.left)
            arr.append(root.val)
            DFS(root.right)
        
        DFS(root)

        return arr[k - 1]
        

        