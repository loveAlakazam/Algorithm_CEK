# -*- coding: utf-8 -*-
#N으로 표현
#참고 URL: https://geonlee.tistory.com/37
import sys
def solution(N, number):
    s=[{N}]
    for i in range(2, 9):
        # (i=2) case_set={NN}
        # (i=3) case_set={NNN}
        # ...
        # (i=8) case_set={NNNNNNNN}
        case_set= { int(str(N) *i)}

        # x는 N이 x_idx+1번 사용하는 경우
        for x_idx in range(int(i/2)):
            #(i=2) 0<= x_idx < 1
            #(i=3) 0<= x_idx < 1
            #(i=4) 0<= x_idx < 2
            #...
            #(i=7) 0<= x_idx < 3
            #(i=8) 0<= x_idx <4
            for x in s[x_idx]:
                # (i=2) (x_idx=0) x는  s[0]의 원소
                # (i=3) (x_idx=0) x는  s[0]의 원소
                # (i=4) (x_idx=0) x는 s[0]의 원소
                # (i=4) (x_idx=1) x는 s[1]의 원소
                for y in s[ i- x_idx- 2]:
                    # (i=2) (x_idx=0) => s[2-0-2]=s[0] => y는 s[0]의 원소
                    # (i=3) (x_idx=0) => s[3-0-2]=s[1] =>  y는 s[1]의 원소
                    # (i=4) (x_idx=0) => s[4-0-2]=s[2] =>  y는 s[2]의 원소
                    # (i=4) (x_idx=1) => s[4-1-2]=s[1]   =>  y는 s[3]의 원소
                    # ...
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(x*y)
                    case_set.add(y-x)
                    if x!=0:
                        case_set.add(y//x)
                    if y!=0:
                        case_set.add(x//y)
                # case_set에 
                if number in case_set:
                    return i
                s.append( case_set)
    return -1


def main():
    N, number = map(int, sys.stdin.readline().strip().split())
    result=solution(N, number)
    print(result)

if __name__=='__main__':
    main()
