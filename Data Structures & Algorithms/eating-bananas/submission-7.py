class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start, end = 0, max(x for x in piles)

        best = end

        middle = (end + start) // 2

        while middle != 0 and start <= end:
            temp = 0
            for i in piles:
                if i % middle == 0:
                    temp += i // middle
                else:
                    temp += i // middle + 1
            if temp <= h:
                best = min(middle, best)
                end = middle - 1
            else:
                start = middle + 1
            
            middle = (end + start) // 2


        return best
