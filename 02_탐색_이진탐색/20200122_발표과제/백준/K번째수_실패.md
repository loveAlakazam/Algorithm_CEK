# 1300. k번째 수

## 실패코드 01

 ```(python)
 # -*- coding: utf-8 -*-
import sys
input= sys.stdin.readline
def binary_search(B,k, N):
    left, right=0, N*N
    while left<=right:
        mid=(left+right)//2
        if mid==k:
            return B[left]
        elif mid>k:
            right=mid-1
        elif mid<k:
            left=mid
    return B[left]

def solution():
    N= int(input())
    k= int(input())
    if N>0 and N<=10**5: #N은 10**5보다 작거나 같은 자연수
        if k>0 and k<=min(10**9, N*N):# k는 min(10**9, N**2)보다 작은 자연수
            B=[0]*(N*N+1)
            for i in range(1,N*N+1):
                if i<=N:
                    B[i]=i
                else:# i>N
                    if i%N==0:
                        B[i]=B[i-N]+N
                    else:
                        B[i]=B[i-N]+(i%N)

            # 오름차순 정렬
            B.sort()
            
            #이진탐색으로 찾는다.
            #print(B[k])
            print(binary_search(B,k, N))
                
if __name__=='__main__':
    solution()

 ```
