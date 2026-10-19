"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        madeNode = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            currNode = queue.popleft()
            for nb in currNode.neighbors:
                if nb not in madeNode:
                    madeNode[nb] = Node(nb.val)
                    queue.append(nb)

        for old, new in madeNode.items():
            new.neighbors = [madeNode[nb] for nb in old.neighbors]


        return madeNode[node]


