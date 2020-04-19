# -*- coding: utf-8 -*-
# 백준 11652 카드
import sys
from collections import Counter
input=sys.stdin.readline

def solution():
    N= int(input()) #카드개수
    cards=[]
    for _ in range(N):
        #N장의 카드 입력받는다
        #strip(): white space 제거
        cards.append(int(input().strip() ))

    # 리스트 cards를 오름차순 정렬한다.
    cards=sorted(cards)
    cards= Counter(cards) #카드 개수 카운트
    print(cards.most_common(1)[0][0]) 

if __name__=='__main__':
    solution()
