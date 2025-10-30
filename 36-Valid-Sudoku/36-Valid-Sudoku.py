class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j]) - 1
                boxIndex = (i // 3) * 3 + (j // 3)

                if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                    return False

                rows[i][num] = cols[j][num] = boxes[boxIndex][num] = 1

        return True
