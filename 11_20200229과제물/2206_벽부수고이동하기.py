# -*- coding: utf-8 -*-
import sys
from collections import deque
N,M =0,0
MAP=None
visited=None
result=1001 #초기화
q=deque()

#현위치의 상/하/좌/우
dy=[-1,1, 0,0]
dx=[0,0,-1, 1]

def isRange(y,x):
    global N,M
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

def bfs():
    global MAP, visited, N, M, result
    while q:
        y,x, d, break_cnt= q.popleft()

        #도착지점 도달하면 종료
        if (y==N-1) and (x==M-1):
            result=d
            break
        
        #현위치의 상/하/좌/우 방문
        for i in range(4):
            nexty=y+dy[i]
            nextx=x+dx[i]
            
            # N행M열 배열의 원소인가?
            if (isRange(nexty, nextx)) and (visited[nexty][nextx]>break_cnt):
                if MAP[nexty][nextx]=='0': #벽이 아닌경우
                    visited[nexty][nextx]=break_cnt
                    q.append((nexty, nextx, d+1, break_cnt))
                    
                else: #벽
                    if break_cnt==0: #벽을 뚫은 횟수가 0번이면
                        visited[nexty][nextx]=break_cnt+1
                        q.append((nexty, nextx, d+1, break_cnt+1))
        
        
def main():
    global N,M, MAP, visited, result
    #N: 세로, M: 가로
    N,M=map(int, sys.stdin.readline().split())
    MAP=[list(sys.stdin.readline().strip()) for _ in range(N)]
    visited=[[1001]*M for _ in range(N)]
    
    #큐에 시작점 먼저 추가(시작점y좌표, 시작점x좌표, 경로개수 1, 벽부수기 횟수 0회)
    q.append((0,0,1,0))
    bfs()
    if result==1001:
        print(-1)
    else:
        print(result)

if __name__=='__main__':
    main()
