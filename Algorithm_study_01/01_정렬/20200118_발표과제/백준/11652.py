# -*- coding: utf-8 -*-
# 백준 11652 카드
import sys
input=sys.stdin.readline

def solution():
    N= int(input()) #카드개수
    cards={}
    for _ in range(N):
        #N장의 카드 입력받는다.
        card=int(input().strip() )#strip(): white space 제거

        # 입력한 card가 cards에 들어있는지 확인
        if card in cards:
            cards[card]+=1
        else:
            cards[card]=1
            
    #딕셔너리 value값(카드 개수)을 기준으로 내림차순 정렬
    cards=sorted(cards.items(), key=lambda x: x[1], reverse=True)

    # max_cnt: 카드개수 최댓값
    max_cnt=cards[0][1]
    #ans: 카드개수가 max_cnt 개이고 카드의숫자가 가장 최소값
    ans=min([card_num for card_num, cnt in cards if cnt==max_cnt])
    print(ans)
if __name__=='__main__':
    solution()
