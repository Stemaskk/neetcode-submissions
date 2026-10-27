# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        start = ListNode(0)
        curr = start

        while l1 or l2 or carry:
            if not l1:
                l1Val = 0
            else:
                l1Val = l1.val

            if not l2:
                l2Val = 0
            else:
                l2Val = l2.val

            sum = l1Val + l2Val + carry
            carry = 0

            if sum >= 10:
                carry = 1
            
            curr.next = ListNode(sum % 10)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return start.next
