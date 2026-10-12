class Solution:
    def findMin(self, nums: List[int]) -> int:
        ndeque = deque(nums)
        
        while ndeque[0] > ndeque[len(nums) - 1]:
            ndeque.appendleft(ndeque.pop())
        
        return ndeque[0]
