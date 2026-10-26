class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        kMax = piles[-1]
        kMin = 1
        result = kMax

        while kMin <= kMax:
            kMid = (kMin + kMax) // 2
            possible = True

            count = 0
            for i in piles:
                if kMid >= i:
                    count += 1
                else:
                    if i % kMid == 0:
                        count += i // kMid
                    else:
                        count += (i // kMid) + 1
                if count > h:
                    possible = False
                    break

            if possible:
                result = kMid
                kMax = kMid - 1

            else:
                kMin = kMid + 1

        return result


