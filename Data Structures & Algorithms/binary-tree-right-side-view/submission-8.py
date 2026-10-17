# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []      
        
        if not root:
            return result
        
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                root = queue.popleft()
                if i == size - 1:
                    result.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
        return result


