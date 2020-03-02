# -*- coding: utf-8 -*-
import sys

def main():
    T=int(sys.stdin.readline())
    for _ in range(T):
        # K: 소설을 구성하는 장의 수 (3<=K<=500)
        K= int(sys.stdin.readline())
        cost=list(map(int, sys.stdin.readline().split()))
        cost.insert(0,0)
        dp=[[0]*(K+1) for _ in range(K+1)] #초기화
        s=[0]*(K+1) #초기화

        for i in range(1,K+1):
            #1부터 i까지의 합
            s[i]=s[i-1]+cost[i]
            
        for d in range(1, K):
            for tx in range(1,K+1-d):#ty=tx+d<=K
                ty=tx+d #ty:도착점
                dp[tx][ty]=10001 #tx->ty까지 최소비용 10001로 초기화

                for mid in range(tx, ty):
                    #tx->ty 까지 도달하는데 최소비용을 구한다.
                    #dp[tx][ty], dp[tx][mid]+dp[mid+1][ty] +s[ty]-s[tx-1]
                    # dp[tx][mid]: tx->mid까지의 최소비용
                    # dp[mid+1][ty]: mid+1-> ty까지의 최소비용
                    # s[ty]-s[tx-1]=  cost[tx]+cost[tx+1]+...+cost[ty]
                    dp[tx][ty]=min(dp[tx][ty], dp[tx][mid]+dp[mid+1][ty]+s[ty]-s[tx-1])
                    
        print(dp[1][K])#1부터 K까지 최소비용
        

if __name__=='__main__':
    main()
