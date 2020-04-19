# -*- coding:utf-8 -*-
import sys
input=sys.stdin.readline

def solution():
    N= int(input())
    d=[]
    for _ in range(N):
        age, name= map(lambda x: int(x) if x.isdigit() else x , input().split())
        d.append([name, age])
    
    # (나이)를 기준으로 정렬
    d.sort(key=lambda x:x[1])

    for name, age in d:
        print(age, name)
    
if __name__=='__main__':
    solution()
