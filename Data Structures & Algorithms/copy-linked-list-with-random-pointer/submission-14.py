"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy = {None: None}
        start = Node(0,head)
        temp = Node(0)
        start.next = head

        while head:
            temp.next = Node(head.val)
            temp = temp.next
            copy[head] = temp
            head = head.next

        head = start.next

        while head:
            copy[head].random = copy[head.random]
            head = head.next

        return copy[start.next]
