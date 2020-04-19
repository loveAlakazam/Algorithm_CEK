# -*- coding: utf-8 -*-
import sys

def main():
    N=int(sys.stdin.readline())
    dp=[ [0]*i  for i in range(1,N+1)]
    a=[ [int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    
    dp[0][0]=a[0][0]
    #r은 0부터 시작
    #r행에 있는 원소개수 r+1개
    for r in range(1,N):
        for c in range(r+1):
            print(r,c, a[r][c], dp[r][c])
            if r==c :
                dp[r][c]=a[r][c]+dp[r-1][c-1]
                
            elif c==0:
                dp[r][0]=a[r][0]+dp[r-1][0]
            elif c>0 and c<r:
                dp[r][c]=a[r][c]+max(dp[r-1][c], dp[r-1][c-1])
    
    print(max(dp[N-1]))
    
if __name__=='__main__':
    main()
