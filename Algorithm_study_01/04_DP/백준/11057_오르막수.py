# -*- coding:utf-8 -*-
import sys
from functools import reduce

def main():
    N=int(sys.stdin.readline())
    dp=[0]*11
    #N=1=> 10 한개
    # n         | 0 1 2 3 4 5 6 7 8 9 10
    # f(n)    |0 0 0 0 0 0 0 0 0 0 1
    # result(1)= n*f(n) 의 합
    dp[10]=1
    for _ in range(1,N+1):# 1부터 N까지 dp 리스트 갱신
        for idx in range(1,11):
            dp[idx] =reduce(lambda x,y: x+y, dp[idx:])
    result=sum(dp)
    print(result%10007)
    
if __name__=='__main__':
    main()
