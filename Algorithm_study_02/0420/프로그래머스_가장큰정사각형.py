from copy import deepcopy
def solution(board):
    row=len(board)
    col=len(board[0])
    answer=max(board[0])
    dp=deepcopy(board)
    for r in range(1,row):
        for c in range(1, col):
            if board[r][c]==1:
                if board[r-1][c-1]==1 and board[r-1][c]==1 and board[r][c-1]==1:
                    dp[r][c]= min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1
                    answer=max(answer, dp[r][c])
    
    return answer**2
