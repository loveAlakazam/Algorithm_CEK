# -*- coding: utf-8 -*-
# 백준- 이분탐색- 10816-숫자카드2
import sys
from collections import Counter
input= sys.stdin.readline       
def find_card(store, need):
    left, right= 0, len(store)-1
    if store[left][0]==need:
        return store[left][1]
    elif store[right][0]==need:
        return store[right][1]
    
    while left<=right:
        mid=(left+right)//2
        if store[mid][0]==need:
            return store[mid][1]
        elif store[mid][0]<need:
            left=mid+1
        elif store[mid][0]>need:
            right=mid-1
    return 0
    
def solution():
    N= int(input())
    # 상근이가 가지고 있는 숫자카드
    store= list(map(int, input().split()))
    
    M= int(input())
    # 상근이가 몇개를 가져야될지 알아봐야하는 M장의 숫자카드
    needs=list(map(int, input().split()))
    
    #상근이가 가지고 있는 숫자카드 N장을 딕셔너리로 정리한다.
    #카드숫자(키값)을 기준으로 오름차순 정렬한다.
    store=sorted(Counter(store).items(), key=lambda x:x[0])
    
    cnts=[]
    # needs에 있는 M장의 카드를 몇개 가지고 있는지 확인
    for need in needs:
        cnts.append(find_card(store,need))
    print(' '.join(map(str,cnts)))

if __name__=='__main__':
    solution()
