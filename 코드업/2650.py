# -*- coding: utf-8 -*-
# 2650. 디지털 도어락
import sys
input=sys.stdin.readline
def get_divider(n):
    d=[1]
    for i in range(2,n+1):
        if n%i==0:
            d.append(i)
    return d        
        
def solution():
    id1, id2, id3= map(int, input().split())
    d1=set(get_divider(id1))
    d2=set(get_divider(id2))
    d3=set(get_divider(id3))
    print(d1,d2,d3)
    # 3개의 수의 최대공약수를 구한다.
    result= max(d1&d2&d3)
    print(result)

if __name__=='__main__':
    solution()
