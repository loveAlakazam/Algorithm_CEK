# -*- coding:utf-8 -*-
# 백준 DP
import sys
input=sys.stdin.readline

def make_one(x):
    result=[0]*(x+1)
    for now in range(2,x+1):
        candidate=[] #후보군
        if now%3==0:# 3으로 나눠지는 수
            candidate.append(result[now//3])
        if now%2==0:# 2으로 나눠지는 수
            candidate.append(result[now//2])
        candidate.append(result[now-1])

        #후보군중 가장 작은값을 찾는다.
        result[now]=min(candidate)+1 
    return result[x]

def solution():
    X=int(input())
    print(make_one(X))

if __name__=='__main__':
    solution()
    # 10을 예제로 한다면
    
    ## index : 0 1 2 3 4 5 6 7 8 9 10
    ## dp    : 0 0 1 1 2 3 2 2 3 2 3
    
    # index=2: dp[2-1],dp[2//2] 중 가장 작은 값 선택(dp[1])=> dp[2]=0+1=1
    # index=3: dp[3-1],dp[3//3] 중 가장 작은 값 선택(dp[1])=> dp[3]=0+1=1
    # index=4: dp[4-1]과 dp[4//2] 중 가장 작은 값 선택(dp[3]=dp[2]=1)=> dp[4]=1+1=2
    # index=5: dp[5-1]만 있으므로 dp[5]=dp[4]+1=3
    
    # index=6: dp[6-1], dp[6//2], dp[6//3] 중 가장 작은 값 선택(dp[3]=dp[2]=1)=> dp[6]=1+1=2
    # dp[5]=3, dp[3]=dp[2]=1 이므로 dp[6]=1+1=2이다.
    
    # index=7: dp[7-1]만 있으므로 dp[7-1]=dp[6]=2
    # index=8: dp[8-1], dp[8//2] 중 가장 작은 값 선택(dp[])-> dp[8]=2+1=3
    # index=9: dp[9-1], dp[9//3] 중 가장 작은 값 선택(dp[3])-> dp[9]=1+1=2
    # index=10: dp[10-1], dp[10//2] 중 가장 작은 값 선택(dp[9]) -> dp[10]=2+1=3
