# -*- coding: utf-8 -*-
import sys
def return_ans(answer):
    return '<'+', '.join(map(str,answer))+'>'
def main():
    N,K =map(int, sys.stdin.readline().split())
    answer=[]
    A=list(range(1,N+1))
    
    #리스트A의 원소는 2개이상일때만
    #A에 남는 원소가 하나가 될때까지
    #큐를 K-1번 회전시켜서 원소를 지워나간다.
    while len(A)>1:
        for _ in range(K-1):
            tmp=A.pop(0)
            A.append(tmp)
        #K-1번 회전시킨 후 A리스트의 맨왼쪽원소를 answer에 넣는다.
        answer.append(A.pop(0))

    #최종적으로 A에 나머지 원소 1개를 마저넣는다 
    answer.append(A[0])
    print(return_ans(answer))
    
    
if __name__=='__main__':
    main()
