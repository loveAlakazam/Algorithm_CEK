# -*- coding: utf-8 -*-
import sys   
def main():
    N= int(sys.stdin.readline())
    lopes=[0]*N
    result=dict()
    
    #N개의 로프 입력받기
    for i in range(N):
        lopes[i]=int(sys.stdin.readline())

    #로프를 오름차순 정렬
    lopes=sorted(lopes)

    #딕셔너리 key값(로프)을 오름차순대로 하여 value값 0으로 초기화
    result[lopes[0]]=0 #맨앞 로프는 먼저 초기화
    for i in range(1,N):
        if lopes[i]==lopes[i-1]:#현재로프가 이전로프와 같다면
            continue
        result[lopes[i]]=0

    #맨처음 로프는 갱신
    result[lopes[0]]=N*lopes[0]
    for i in range(1,N):
        if lopes[i]==lopes[i-1]:
            continue
        result[lopes[i]]=lopes[i]*(N-i)

    print(result)
    #result를 value값을 기준으로 내림차순 정렬
    result=sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(result[0][1])
        
if __name__=='__main__':
    main()
