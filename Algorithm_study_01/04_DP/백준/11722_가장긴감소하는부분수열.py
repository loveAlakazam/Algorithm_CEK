# -*- coding: utf-8 -*-
# 가장긴 감소하는 부분수열
import sys

def main():
    N=int(sys.stdin.readline())
    A=list(map(int, sys.stdin.readline().split() ))
    dp=[1]*N
    for now in range(1,N):
        for prev in range(now):
            if A[now]<A[prev]:
                dp[now]=max(dp[now], dp[prev]+1)
    print(max(dp))

if __name__=='__main__':
    main()


