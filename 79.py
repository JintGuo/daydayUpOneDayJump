class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, column, word_pos):
            if not 0<=row<len(board) or not 0<=column<len(board[0]) or board[row][column]!=word[word_pos]:
                return False
            if word_pos == len(word) - 1: return True
            
            tmp, board[row][column]=board[row][column], 'Occupied'
            res = dfs(row+1, column, word_pos+1) or dfs(row-1, column, word_pos+1) or dfs(row, column+1, word_pos+1) or dfs(row, column-1, word_pos+1)
            board[row][column] = tmp
            return res
    

        for row in range(len(board)):
           for column in range(len(board[0])):
                res= dfs(row, column, 0)
                if res ==True:
                    return True
        
        return False
