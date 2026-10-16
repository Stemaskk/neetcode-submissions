# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        result = []

        if not root:
            return result

        while queue:
            result.append([])
            for i in range(len(queue)):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)
                
                result[-1].append(currNode.val)
        
        return result


