class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row =defaultdict(set)
        hash_col =defaultdict(set)
        hash_sq =defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    index = (i // 3) * 3 + j//3
                    if (board[i][j] in hash_row[i]
                        or board[i][j] in hash_col[j] 
                        or board[i][j] in hash_sq[index]):
                        return False
                    else:
                        hash_row[i].add(board[i][j])
                        hash_col[j].add(board[i][j])
                        hash_sq[index].add(board[i][j])
        return True