# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = set()
        
        while head:
            curr = head
            head = head.next

            if curr in seen:
                return True
            seen.add(curr)

        return False