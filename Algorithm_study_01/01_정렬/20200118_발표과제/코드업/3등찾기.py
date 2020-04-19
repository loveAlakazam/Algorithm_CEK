# -*- coding: utf-8 -*-
# code-up : 1420
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
input=sys.stdin.readline

def solution():
    N=int(input())
    scores={}
    for _ in range(N):
        name, score= map(lambda x: int(x) if x.isdigit() is True else x , input().split())
        print(name, score)
        scores[name]=score

    #sorted는 오름차순 정렬
    #reversed는 내림차순정렬
    # 딕셔너리 value기준 정렬 => sorted( 딕셔너리.items(), reverse=여부)
    scores=sorted(scores.items() ,key=lambda x:x[1], reverse=True)
    print(scores)
    print(scores[2][0])

if __name__=='__main__':
    solution()
