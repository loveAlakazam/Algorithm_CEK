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
