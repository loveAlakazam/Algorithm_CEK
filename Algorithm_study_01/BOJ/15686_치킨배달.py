import sys
from itertools import combinations
input=sys.stdin.readline
#N:2~50, M:1~13
N,M= map(int, input().strip().split())
MAP=[ [*map(int, input().strip().split())] for _ in range(N)]

#1. 집좌표와 치킨집 좌표를 구한다.
chickens=[]
houses=[]
for y in range(N):
    for x in range(N):
        if MAP[y][x]==1:
            houses.append((y,x))
            
        elif MAP[y][x]==2:
            chickens.append((y,x))

#집좌표의 각원소들의 치킨거리를 구한다.
chicken_street={}
for house in houses:
    hy, hx= house
    for chicken in chickens:
        cy, cx=chicken
        chicken_street[(hy,hx,cy,cx)]=abs(hy-cy)+abs(hx-cx)

#combinations 라이브러리를 이용하여 치킨집M개를 뽑는다.
cases=[*combinations(chickens,M)]
result=float('inf')
for case in cases:
    street=0
    for house in houses:
        hy, hx= house
        tmp=float('inf')
        #집좌표(hy, hx)의 치킨거리를 찾는다.
        for c in case:
            cy,cx=c
            tmp=min(tmp, chicken_street[(hy,hx,cy,cx)])
        street+=tmp
    result=min(result, street)

print(result)
