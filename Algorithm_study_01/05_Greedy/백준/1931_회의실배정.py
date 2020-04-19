# -*- coding: utf-8 -*-
# 1931. 회의실 배정
# 참고url: https://kim6394.tistory.com/67
import sys
# operator모듈함수는 다중 수준의 정렬을 허용합니다.
# key는 정렬기준이 1개라면 lambda x: x[0], lambda x: x[1]
# itemgetter은 정렬기준이 2개이상일때 사용
# 회의 끝나는시간 을 기준으로 먼저 정렬(기준1: 회의끝나는 시간이 작은 순)
# 기준1이 서로 같은경우 기준2인 회의 시작한 시간을 기준으로 정렬합니다.
# 참고url: https://docs.python.org/ko/3/howto/sorting.html#operator-module-functions
from operator import itemgetter
    
def main():
    points=[]
    N= int(sys.stdin.readline())
    for n in range(N):
        points.append(tuple(map(int,sys.stdin.readline().split())))

       
    print(points)
    #회의끝나는 시간을 기준으로 오름차순 정렬
    #회의끝나는 시간이 서로 같다면 회의시작시간이 작은것을 우선순위로합니다.
    points=sorted(points, key=itemgetter(1,0) )
    print(points)

    result=0
    last=0
    for idx, p in enumerate(points):
        # s: 회의 시작 시간
        # e: 회의 끝나는 시간
        s,e= map(int, p)
        
        # 맨처음은 들어오게 합니다.
        if idx==0:
            last=e
        else:
            # 다음 회의의 시작시간이 이전회의의 끝나는 시간보다 크거나 같다면
            # 현재까지 마친 회의중 마지막 시간을 업데이트합니다.
            if last<=s:
                last=e
                result+=1
                
    print(result+1)#맨처음 회의시간 덧셈고려.         

if __name__=='__main__':
    main()
