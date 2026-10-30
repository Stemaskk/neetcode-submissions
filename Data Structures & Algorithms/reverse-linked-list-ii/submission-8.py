# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        start = ListNode(0, head)
        prev = start

        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        for i in range(right - left):
            move = curr.next
            curr.next = move.next
            move.next = prev.next
            prev.next = move

        return start.next