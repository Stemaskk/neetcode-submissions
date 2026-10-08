class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        answer = []
        for _ in range(k):
            best = max(counts, key=counts.get)
            answer.append(best)
            del counts[best]
        return answer
        