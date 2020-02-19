# -*- coding: utf-8 -*-
import sys
from collections import deque 
cabbages=None
dy=[-1,1,0,0]
dx=[0,0,-1,1]
N, M=0,0
q= deque()

#N*M열에 적절한 위치에  있는가?
def isRange(y,x):
    global N, M
    if (y>=0 and y<N) and(x>=0 and x<M):
        return True
    return False


def bfs():
    global cabbages, visited
    while q:
        y, x= q.popleft()
        #만일 방문하지 않은 상태라면
        if not visited[y][x]:
            visited[y][x]=True
            
            #현위치의 상/하/좌/우
            for i in range(4):
                nexty=y+dy[i]
                nextx=x+dx[i]

                #적절한 위치에 있는가?
                if isRange(nexty, nextx):
                    #아직 방문하지 않았고, 1이라면?
                    if (cabbages[nexty][nextx]==1)and(not visited[nexty][nextx]):
                        #큐에 추가
                        q.append((nexty, nextx))
                        
def main():
    global cabbages, N, M, visited
    
    T=int(sys.stdin.readline())
    for _ in range(T):
        #M; 배추밭 가로길이(열)
        #N: 배추밭 세로 길이(행)
        #K: 배추가 심어진 위치 개수
        M, N, K= map(int, sys.stdin.readline().split())
        cabbages=[[0]*M for _ in range(N)] #배추초기화
        visited=[[False]*M for _ in range(N)]#방문리스트 초기화

        # K개의 배추의 위치 입력
        for _ in range(K):
            x,y=map(int, sys.stdin.readline().split())
            cabbages[y][x]=1

        #BFS로 탐색하여 배추그룹의 개수를 찾는다.
        cnt=0
        for y in range(N):
            for x in range(M):
                #아직 방문하지 않은 상태이고 1이라면.
                #bfs로 연결된 배추 탐색후 -> cnt증가
                if (cabbages[y][x]==1) and (not visited[y][x]):
                    #현재위치를 큐에 넣어서 -> bfs탐색
                    q.append((y,x))
                    bfs()
                    cnt+=1
        print(cnt)

if __name__=='__main__':
    main()
