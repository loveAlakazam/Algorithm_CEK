# -*- coding: utf-8 -*-
import sys
    
def main():
    N=int(sys.stdin.readline())
    #(n=1) dp[0]=1
    dp=[1]*N
    if N>=2:
        #(n=2) dp[1]=2
        dp[1]=2

        #(n=3 ~ n=N) dp[n]=dp[n-1]+dp[n-2]
        for i in range(2,N):
            dp[i]=dp[i-1]+dp[i-2]
    print(dp[N-1]%10007)

if __name__=='__main__':
    main()
