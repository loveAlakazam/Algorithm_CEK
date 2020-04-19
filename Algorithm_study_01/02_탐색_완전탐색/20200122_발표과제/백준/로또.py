# -*- coding: utf-8 -*-
#백준-완전탐색-6603- 로또
import sys
from itertools import combinations
input= sys.stdin.readline

def solution():
    #49개(1~49)의 숫자 중 6개를 고른다..
    #49가지 수중 k(k>6)개의 수를 골라서 집합 S를 만든다.
    #그 수만 가지고 번호를 선택
    # 집합 S와 k가 주어졌을 때..
    # 수를 고르는 모든 방법을 구하는 프로그램...

    while True:
        # 숫자 입력
        lotto=list(map(int, input().split()))

        #맨 앞에 있는 숫자가 0이면 while-loop을 나간다.
        if lotto[0]==0:
            break
        
        #0번째수를 pop해서 k에 저장
        #나머지는 S에 포함되는 수이다.
        k=lotto.pop(0)
        if k>6 and k<13:
            # k개의 숫자 중 6개를 골라서 얻게되는 경우를 구한다.
            cases=list(combinations(lotto,6))
            for case in cases:
                print(' '.join(str(c) for c in case))
        print()
    
if __name__=='__main__':
    solution()
