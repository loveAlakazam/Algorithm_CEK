# -*- coding: utf-8 -*-
import sys
def main():
    result=0
    N= int(sys.stdin.readline())
    
    dp=[ [0]*3 for _ in range(N)] 
    cost=[]
    for i in range(N):
        cost.append(list(map(int, sys.stdin.readline().split())))

    dp[0][0]=cost[0][0]
    dp[0][1]=cost[0][1]
    dp[0][2]=cost[0][2]
    for i in range(1,N):
        # R선택
        dp[i][0]=cost[i][0]+min(dp[i-1][1], dp[i-1][2])

        # G선택
        dp[i][1]=cost[i][1]+min(dp[i-1][0], dp[i-1][2])

        # B선택
        dp[i][2]=cost[i][2]+min(dp[i-1][0], dp[i-1][1])
        
    print(min(dp[N-1]))
    #메모리를 아끼기위해 지운다.
    del cost
    del dp

if __name__=='__main__':
    main()
