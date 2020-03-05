# -*- coding: utf-8 -*-
# backtracking 훈련: 암호만들기
import sys
input= sys.stdin.readline

L,C=0,0
words=None
vowels={'a','e','i','o','u'} #모음 집합
consonant=set(chr(n) for n in range(97,97+26) if chr(n) not in vowels )#자음

# idx: 알파벳(words)의 인덱스
# password: 만들수 있는 암호
# vow: 모음개수
# cons: 자음개수
def backtracking(idx , pw, vow, cons ):
    global L,C, words, visited
    #만일 pw길이가 L이라면
    if len(pw)==L:
        #최소 1개 이상의 모음을 갖는가?/ 최소 2개 이상의 자음을 갖는가?
        if (vow>=1) and (cons>=2):
            print(pw)
        
    #pw의 길이가 L보다 작다면
    elif len(pw)<L:
        for i in range(idx+1, C):
            if words[i] in vowels: #다음알파벳이 모음이라면
                backtracking(i, pw+words[i], vow+1,cons)
            else:#다음 알파벳이 자음이라면
                backtracking(i, pw+words[i], vow, cons+1)

def main():
    global L,C, words, visited
    
    #L: 암호길이/ C: words의 길이. (3<=L<=C<=15)
    L,C=map(int, input().split())
    words=sorted([*(input().split())]) #오름차순으로 정렬.

    #가능한 암호의 시작점: 0,1, .., C-L
    for i in range(C-L+1):
        if words[i] in vowels:
            backtracking(i, words[i],1,0)
        else:
            backtracking(i, words[i],0,1)
        

if __name__=='__main__':
    main()
