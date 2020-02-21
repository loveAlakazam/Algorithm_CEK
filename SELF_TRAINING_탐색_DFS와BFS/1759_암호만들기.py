# -*- coding: utf-8 -*-
import sys
import itertools
       
def main():
    L,C= map(int, sys.stdin.readline().split())
    input_alpha=sorted(sys.stdin.readline().strip().split(), key=str)

    #자음만 분리
    consonants=sorted(filter(lambda x: x not in ('a','e','i','o','u'), input_alpha),key=str)
    #모든경우
    all_cases= itertools.combinations(input_alpha,L)
    if len(consonants)>=L:
        #알파벳CL - 자음CL
        all_cases=set(all_cases)-set(itertools.combinations(consonants,L))
        
    all_cases=sorted(all_cases, key=str)
    for case in all_cases:
        print(''.join(case))

if __name__=='__main__':
    main()
