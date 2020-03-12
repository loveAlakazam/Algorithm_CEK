import sys
from copy import deepcopy
from collections import deque

sys.setrecursionlimit(10**6)
input=sys.stdin.readline
q=deque()

N,M=0,0
MAP=None
visited=None

#북/동/남/서
dy=[-1,0, 1, 0]
dx=[0,1,0,-1]

def isRange(y,x):
    global N,M
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

       
#d: 현재방향
#d=0(북)의 왼쪽방향 d_left=3(서)/ 후진:d_back=2(남)
#d=1(동)의 왼쪽방향 d_left=0(북)/ 후진:d_back=3(서)
#d=2(남)의 왼쪽방향 d_left=1(동)/ 후진:d_back=0(북)
#d=3(서)의 왼쪽방향 d_left=2(남)/ 후진:d_back=1(동) 방향은 d그대로 유지
def now_left_and_back(d):
    if d==0:#북
        return 3,2 #왼쪽방향, 후진방향
    elif d==1:#동
        return 0,3
    elif d==2:#남
        return 1,0
    #서
    return 2,1

def bfs():
    global N,M, MAP, visited
    
    while q:
        y,x,d=q.popleft()
        #현재방향을 복사하여, 2-a/b 과정의 탐색용으로 한다.
        d_copy=deepcopy(d)

        #방문했는지 확인
        if not visited[y][x]:
            visited[y][x]=True

        #2-a/b과정에서 왼쪽공간을 찾은 경우에는 2-c를 수행하지 못하도록함.
        isStop=False
        
        #(2-a/b과정). 현재방향을 기준으로 왼쪽방향에 청소할 수 있는지 탐색
        for _ in range(4): #최대회전수 4번
            #현재방향의 왼쪽방향과 후진방향
            d_left, d_back= now_left_and_back(d_copy)
            lefty, leftx= y+dy[d_left], x+dx[d_left]
            if (MAP[lefty][leftx]==0) and (not visited[lefty][leftx]):
                q.append((lefty, leftx, d_left))
                isStop=True
                break
            #현재방향의 왼쪽방향으로 기준방향으로 한다.
            d_copy=d_left
            
        #(2-a/b과정을 수행하지 못했다면)
        if not isStop:
            #2. 네방향이 이미 청소되거나 벽인경우
            #방향(d)를 그대로 유지한채 후진이 가능한지 확인
            _ , d_back=now_left_and_back(d)
            backy, backx= y+dy[d_back], x+dx[d_back]
            if (MAP[backy][backx]==0):
                q.append((backy, backx, d))

def main():
    global N,M, MAP, visited
    #N: 세로, M:가로
    N,M= map(int, input().strip().split())
    
    #초기 로봇청소기의 위치(r,c)와 바라보는 방향
    #(d=0) 북 / (d=1) 동 / (d=2) 남 / (d=3) 서
    r,c,d=map(int, input().strip().split())

    #장소맵그리기
    MAP=[]
    for y in range(N):
        MAP.append([*map(int, input().strip().split())])

    #방문리스트 만들기
    visited=[[False]*M for _ in range(N)]
    q.append((r,c,d))
    bfs() #bfs탐색
    
    #visited가 True인것 개수를 카운트
    ans=0
    for y in range(N):
        for x in range(M):
            if visited[y][x]==True:
                ans+=1
    print(ans)

if __name__=='__main__':
    main()
