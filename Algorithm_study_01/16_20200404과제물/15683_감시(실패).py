import sys
from copy import copy

input= sys.stdin.readline
min_blind_spot=float('inf') #초기화
q=deque()

#방향
#1: 오른쪽/왼쪽/ 위/ 아래 
#2: 왼쪽+오른쪽 / 위+아래 
#3: 위+오른쪽/ 오른쪽+아래/ 왼쪽+아래/ 왼쪽+위 
#4: 왼쪽+오른쪽+위 / 왼쪽+오른쪽+아래/ 왼쪽+위+아래/ 오른쪽+위+아래
#5: 왼쪽+오른쪽+위+아래
def 

def isRange(y,x):
    global N,M
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

def zero_count(MAP):
    global N,M
    cnt=0
    for y in range(N):
        for x in ragne(M):
            if MAP[y][x]==0:
                cnt+=1
    return cnt

def dfs2(nowy, nowx, MAP, d):
    #현위치의 값이 6이 아니라면
    if MAP[nowy][nowx]!=6:
        dy, dx= d
        nexty=nowy+dy
        nextx=nowx+dx
        if isRange(nexty, nextx):
            if MAP[nexty][nextx]!=6: #다음이 벽이 아니라면
                MAP[nexty][nextx]='#'
                return dfs2(nexty, nextx, MAP,d)
    return MAP #새로 업데이트한 맵을 리턴.
        

def dfs(cury, curx, MAP, visited):
    global N,M, min_blind_spot
    nexty, nextx= cury, curx
    
    for y in range(cury, N):
        for x in range(curx, M):
            if (MAP[y][x]>=1 and MAP[y][x]<=5) and (visited[y][x]==0):
                nexty, nextx= y,x
                visited[nexty][nextx]=1#방문
                break
    print('nexty: {}, nextx: {}\ncury: {}, curx: {}'.format(nexty, nextx, cury, curx))
    
    #더이상 1~5인 곳이 없다면-> zero_count한다.
    if (nexty==cury) and (nextx==curx):
        min_blind_spot=min(min_blind_spot, zero_count(MAP))

    #nexty, nextx에 해당하는 값에 따라서 다양한 MAP을 만든다.
    direction=MAP[nexty][nextx]
    for i in range(len(DY[val])):
        dfs(nexty, nextx, tmp_map, tmp_visited)
                
            

# N: 세로크기, M: 가로크기
N, M = map(int, input().strip().split())
MAP= [[*map(int, input().strip().split())] for _ in range(N)]
visited={}

#방문리스트 초기화
for y in range(N):
    for x in range(M):
        visited[(y,x)]=0
        
dfs(0,0,MAP, visited)
print(min_blind_spot) #사각지대의 최솟값을 구한다.






