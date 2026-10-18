class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        result = []

        def backtrack(index, array, total):
            if total >= target or index == len(candidates):
                if total == target:
                    result.append(array[:])
                return
            
            array.append(candidates[index])
            backtrack(index + 1, array, total + candidates[index])
            array.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
                
            backtrack(index + 1, array, total)

        backtrack(0, [], 0)

        return result
