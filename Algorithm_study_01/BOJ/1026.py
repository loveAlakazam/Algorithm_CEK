# -*- coding: utf-8 -*-
# 백준 - 이진탐색- 보물- 1026
import sys
input=sys.stdin.readline

def solution():
    N=int(input())
    # 오름차순 정렬
    A=sorted(list(map(int, input().split())))

    #내림차순 정렬
    B=sorted(list(map(int,input().split())), reverse=True)
    print(sum(a*b for a,b in zip(A,B)))
        

if __name__=='__main__':
    solution()
    
