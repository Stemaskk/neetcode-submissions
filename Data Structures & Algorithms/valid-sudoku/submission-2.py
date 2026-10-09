class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = set()
            for j in i:
                if j == ".":
                        continue
                if j in row:
                    return False
                row.add(j)
        
        for i in range(9):
            col = set()
            for j in board:
                if j[i] == ".":
                    continue
                if j[i] in col:
                    return False
                col.add(j[i])
        
        for i in range(0, 9, 3):
            boxes = [set(), set(), set()]
            for j in range(3):
                for k in range(9):
                    val = board[i + j][k]
                    if val == ".":
                        continue
                    if val in boxes[k // 3]:
                        return False
                    boxes[k // 3].add(val)

        return True