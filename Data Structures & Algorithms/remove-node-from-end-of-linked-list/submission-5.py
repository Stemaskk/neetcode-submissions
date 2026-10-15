# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        temp = head
        count = 0

        while temp:
            temp = temp.next
            count += 1

        temp = start
        for i in range(count - n):
            temp = temp.next

        temp.next = temp.next.next

        return start.next