# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ldeque = deque()
        curr = head
        back = False
        length = 0

        while curr:
            ldeque.append(curr)
            curr = curr.next
            length += 1

        curr = head

        for i in range(length):
            if not back:
                curr.next = ldeque.popleft()
                back = True
            else:
                curr.next = ldeque.pop()
                back = False
            curr = curr.next

        curr.next = None
