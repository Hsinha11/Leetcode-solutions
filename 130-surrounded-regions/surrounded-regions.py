class Solution:
    def dfs(self,i,j,n,m,board):
        board[i][j]='S'
        d= [(0,-1),(-1,0),(0,1),(1,0)]
        for r,c in d:
            nr = i+r
            nc = j+c
            if nr in range(n) and nc in range(m) and board[nr][nc]=='O':
                # board[nr][nc]='S'
                self.dfs(nr,nc,n,m,board)
        return 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # print(board)
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O' and (i==0 or i==n-1 or j==0 or j==m-1):
                    self.dfs(i,j,n,m,board)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
        for i in range(n):
            for j in range(m):
                if board[i][j]=='S':
                    board[i][j]='O'    
        print(board)