# -*- coding: utf-8 -*-
# 참고: https://it-and-life.tistory.com/136
# 1890. 점프
import sys
        
def main():
    N=int(sys.stdin.readline())
    A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    board=[ [0]*N for _ in range(N)]
    print(A)
    
    board[0][0]=1
    for r in range(N):
        for c in range(N):
            jump=A[r][c]
            if r<N-1 and r+jump<N:
                board[r+jump][c]+=board[r][c]
              
            if c<N-1 and c+jump<N:
                board[r][c+jump]+=board[r][c]
    print(board[N-1][N-1])

if __name__=="__main__":
    main()
