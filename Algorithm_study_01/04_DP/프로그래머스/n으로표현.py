# -*- coding: utf-8 -*-
# 참고url: https://gurumee92.tistory.com/164
import sys
def solution(N, number):
    answer=0
    # (1) s: 숫자 최소1번~ 최소8번 사용했을 때 얻을 수 있는 숫자들의 집합이다.
    # 숫자 N을 사용횟수의 최솟값은 8이하이므로
    # 8번을 넘으면 -1을 반환한다.
    # 숫자 N을 1번 이용해서 만들 수 있는 숫자
    # -> N
    #
    # 숫자 N을 2번 이용해서 만들 수 있는 숫자
    #-> NN, N+N, N-N(0), N*N, N/N(1)
    #
    # 숫자 N을 3번이용해서 만들 수 있는 숫자
    #-> NNN,
    #-> NN+N, NN-N, NN*N, NN/N
    #-> (N+N)+N, (N+N)-N, (N+N)*N, (N+N)/N
    #-> (N-N)+N, (N-N)-N, (N-N)*N(0), (N-N)/N(0)
    #-> (N*N)+N, (N*N)-N, (N*N)*N, (N*N)/N
    #-> (N/N)+N, (N/N)-N, (N/N)*N, (N/N)/N(0)
    s= [ set() for x in range(8) ] #만들수있는 숫자 중, 중복되는 숫자가 있다.

    #(2) 각 set마다 기본수 N*i 수 초기화
    # s=[ {N}, {NN}, {NNN}, ... , {NNNNNNNN}]
    for i,x in enumerate( s, start=1):
        x.add( int(str(N) *i) )

    #(3)
    # N은 1~9 에 해당하는 숫자이다.
    # N을 X번 사용= [ {(N을 1번 사용) + (N을 X-1번 사용)} ,
    #                            {(N을 2번 사용) + (N을 X-2번 사용)},
    #                            {(N을 3번 사용) + (N을 X-3번 사용)}, ...
    #                            {(N을 X-1번 사용)+ (N을 1번 사용)} ]
    for i in range(1, 8): #N 최소 사용횟수 : 1~8
        for j in range(i):  
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2!=0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1
            break
        else:
            answer-=1
    return answer

def main():
    N, number= map(int, sys.stdin.readline().strip().split())
    if (N>=1 and N<=9) and (number>=1 and number<=32000):
        print(solution(N,number))
    
if __name__=='__main__':
    main()
