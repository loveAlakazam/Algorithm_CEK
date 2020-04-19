# -*- coding: utf-8 -*-
# DP-  오르막수
import sys
def main():
    N= int(sys.stdin.readline())
    dp=[ [0]*10 for _ in range(N)]
    
    #N=1일때 dp[0][1,2,...,9]=1
    for k in range(10):
        dp[0][k]=1
        
    # n=2,3,4,..,N
    # k=0,1,2,...,9
    # dp[n][k] : 숫자의 길이가 n이고, 마지막숫자가 k인 오르막수
    # dp[n][k]= dp[n-1][0]+dp[n-1][1]+...+dp[n-1][k-1]+dp[n-1][k]
    # N=1일때 dp 행번호는 0이므로
    # N=n(2,3,4,...,N)일때 행번호는 n-1이다.
    
    for n in range(1,N):
        for k in range(10):#dp[n][k]
            for c in range(k+1):#dp[n-1][0]+dp[n-1][1]+...+dp[n-1][k]
                dp[n][k]+=dp[n-1][c]
                
    # dp의 N-1행인 열들 계산
    result=0
    for k in range(10):
        result+=dp[N-1][k]
    print(result%10007)
    
if __name__=='__main__':
    main()
