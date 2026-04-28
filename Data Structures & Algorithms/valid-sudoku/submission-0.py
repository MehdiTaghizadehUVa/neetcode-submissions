class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row =defaultdict(list)
        hash_col =defaultdict(list)
        hash_sq =defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":

                    if board[i][j] in hash_row[i]:
                        return False
                    else:
                        hash_row[i].append(board[i][j])

                    if board[i][j] in hash_col[j]:
                        return False
                    else:
                        hash_col[j].append(board[i][j])

                    index = (i // 3) * 3 + j//3

                    if board[i][j] in hash_sq[index]:
                        return False
                    else:
                        hash_sq[index].append(board[i][j])
        return True