# -*- coding: utf-8 -*-
import sys
def main():
    N=int(sys.stdin.readline())
    A=list(map(int, sys.stdin.readline().split()))
    dp=[0]*N
    dp[0]=A[0]
    for now in range(1,N):
        for prev in range(now):
            if A[prev]<A[now]:
                dp[now]=max( dp[now], dp[prev])
        dp[now]+=A[now]
    print(max(dp))

if __name__=="__main__":
    main()
