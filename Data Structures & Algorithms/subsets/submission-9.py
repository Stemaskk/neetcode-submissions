class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def DFS(index: int, array: List) -> None:
            if index == len(nums):
                result.append(array[:])
                return
            
            DFS(index + 1, array)

            array.append(nums[index])
            DFS(index + 1, array)
            array.pop()
        
        DFS(0, [])

        return result