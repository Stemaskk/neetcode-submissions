class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        start, end = 0, len(matrix) * length - 1

        while start <= end:
            middle = (start + end) // 2
            mrow, mcol = middle // length, middle % length
            if matrix[mrow][mcol] == target:
                return True
            elif matrix[mrow][mcol] < target:
                start = middle + 1
            else:
                end = middle - 1

        return False