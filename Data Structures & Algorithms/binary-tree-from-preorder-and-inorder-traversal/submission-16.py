# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        size = len(preorder)
        idxInorder = {}

        for i in range(size):
            idxInorder[inorder[i]] = i

        def makeNode(preStart, preEnd, inStart, inEnd):

            if preStart > preEnd:
                return None

            middle = idxInorder[preorder[preStart]]
            leftSize = middle - inStart
                
            leftSub = makeNode(preStart + 1, preStart + leftSize, inStart, middle - 1)

            rightSub = makeNode(preStart + leftSize + 1, preEnd, middle + 1, inEnd)

            return TreeNode(preorder[preStart], leftSub, rightSub)

        return makeNode(0, size - 1, 0, size - 1)
