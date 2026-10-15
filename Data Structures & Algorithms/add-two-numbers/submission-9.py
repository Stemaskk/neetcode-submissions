# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        3 2 1
        6 5 4

        Ones add each other, stored in output linkedlist

        Maybe we can modify original Linkedlist?

        Assume not

        Each digits do not impact each other unless there is an overflow:

        Flag? that can keep if there is an overflow

        Doing this addition would have O(n) since we are only treversing through the two linked list once


        """

        overflow = 0
        result = ListNode(0)
        start = result

        while l1 or l2 or overflow:
            valsum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + overflow

            overflow = valsum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            result.next = ListNode(valsum % 10)

            result = result.next


        return start.next
