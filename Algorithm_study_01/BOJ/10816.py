# -*- coding: utf-8 -*-
# 백준- 이분탐색- 10816-숫자카드2
import sys
from collections import Counter
input= sys.stdin.readline       
    
def solution():
    N= int(input())
    # 상근이가 가지고 있는 숫자카드
    store= list(map(int, input().split()))
    
    M= int(input())
    # 상근이가 몇개를 가져야될지 알아봐야하는 M장의 숫자카드
    needs=list(map(int, input().split()))

    #상근이가 가지고 있는 숫자카드 N장을 딕셔너리로 정리한다.
    store=Counter(store)

    cnts=[]
    # needs에 있는 M장의 카드를 몇개 가지고 있는지 확인
    for need in needs:
        cnts.append(store[need])
    print(' '.join(map(str,cnts)))

if __name__=='__main__':
    solution()
