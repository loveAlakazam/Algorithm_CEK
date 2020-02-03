# -*- coding: utf-8 -*-
# greedy: 동전0
import sys

def main():
    N, K= map(int, sys.stdin.readline().split() )
    A= [ int(sys.stdin.readline().strip()) for _ in range(N)]
    #가장 큰단위의 화폐부터 시작한다.
    A= sorted(A ,reverse=True)
    
    result=0
    for m in A:
        # K가 m보다 크면
        if K>0 and K>=m:
            #divmod(큰수, 작은수)=(몫, 나머지)
            # K//m (몫)-> 동전개수 카운트
            # K%m(나머지)-> K갱신..
            cnt,K=divmod(K, m)
            result+=cnt
    print(result)

if __name__=='__main__':
    main()


