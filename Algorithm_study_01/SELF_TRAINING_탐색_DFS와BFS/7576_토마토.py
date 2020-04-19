# -*- coding: utf-8 -*-
import sys
from collections import deque
#M:가로(열), N:세로(행)
#tomatoes: 토마토
M,N= map(int, sys.stdin.readline().split())
tomatoes=[ list(map(int,sys.stdin.readline().split()))  for _ in range(N)]
q=deque()
visited=[ [False]*M for _ in range(N)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def isRange(y,x):
    global N,M
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

def bfs():
    global visited, tomatoes
    while q:
        cury, curx, day=q.popleft()
        if not visited[cury][curx]:
            #방문하지 않았다면, 방문상태로 만든다.
            visited[cury][curx]=True

            #(cury, curx)의 상하좌우를 찾는다
            #그 상/하/좌/우가 적절한 위치인지 확인한다.
            for i in range(4):
                nexty=cury+dy[i]
                nextx=curx+dx[i]

                #(nexty, nextx)가 적절한 위치에 있는가?
                if isRange(nexty, nextx):
                    #(nexty, nextx)에 위치한 토마토가
                    #아직 방문하지 않은 상태이고, 익지않은 토마토(0)이라면
                    if (tomatoes[nexty][nextx]==0) and (not visited[nexty][nextx]):
                        tomatoes[nexty][nextx]=1 #그토마토는 이제 익은상태로 한다.
                        q.append((nexty, nextx, day+1)) #큐에 넣는다.
    return day

def print_tomatoes():
    global tomatoes
    for t in tomatoes:
        print(t)
    print()

def main():
    global N,M, tomatoes, visited
    #1. 안익은 토마토(0)가 있는지 확인한다
    day=0 #모든 토마토가 익을 때까지 걸린시간(일)
    cnt_green=0
    for y in range(N):
        for x in range(M):
            #안익은 토마토가 있다면 나간다.
            if tomatoes[y][x]==0:
                cnt_green+=1
                break

    #안익은 토마토가 최소 한개라도 있다면..
    if cnt_green>=1:
        #모든 토마토가 익을때 까지 걸리는 시간(일)
        #2. 안익은 토마토가 있다면
        #방문하지 않은 상태인, 익은 토마토를 찾는다.
        for y in range(N):
            for x in range(M):
                if (tomatoes[y][x]==1) and (not visited[y][x]):
                    #일단 큐에 넣는다.
                    q.append((y,x,0))
                    
        #bfs를 실행한다
        day=bfs()
        #3. 아직도 안익은 토마토가 존재한다면?
        for y in range(N):
            for x in range(M):
                if tomatoes[y][x]==0:
                    day=-1
                    break
    print(day)

if __name__=='__main__':
    main()

