#-*- coding: utf-8 -*-
# brute force: 백준 - 123더하기 9095
import sys
input=sys.stdin.readline

def solution():
    # 테스트 케이스
    T=int(input())
    for _ in range(T):
        # 정수 입력
        n=int(input())
        #정수 n은 양수이며, 11보다 작다.
        if n>0 and n<11:
            arr=11*[0]
            arr[1]=1
            arr[2]=2
            arr[3]=4
            for i in range(4,n+1):
                arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
            print(arr[n])

if __name__=='__main__':
    solution()
    # (n=1) 1 -->  dp[1]=1
    # (n=2) 1+1, 2 --> dp[2]=2
    # (n=3) 1+1+1,  1+2(2개),  3 --> dp[3]=4
    # (n=4) 1+1+1+1,  1+1+2(3개), 1+3(2개), 2+2 --> dp[4]=7

    # (n=5) 1+1+1+1+1, 1+1+1+2(4개), 1+1+3(3개), 1+2+2(3개), 2+3(2개)
    # --> dp[5]=13

    # (n=6) 1+1+1+1+1+1, 1+1+1+1+2(5개), 1+1+1+3(4개), 1+1+2+2(6개=4!/2!*2!),
    #            1+2+3(3!=6개), 2+2+2, 3+3     --> dp[6]=24

    # dp=[0,1,2,4,7,13,24, 44, ...]
    # dp[4]=7=dp[3]+dp[2]+dp[1]
    # dp[5]=13=dp[4]+dp[3]+dp[2]
    # dp[6]=24=dp[5]+dp[4]+dp[3]
    # dp[7]=44=dp[6]+dp[5]+dp[4]
    # (n>=4) dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
