import sys
from queue import PriorityQueue
from copy import deepcopy
input=sys.stdin.readline
q=PriorityQueue()

#상하좌우
dy=(-1,1,0,0) 
dx=(0,0,-1,1)

#M: 가로크기
#N: 세로크기
M,N=map(int, input().strip().split())
MAP=[[*map(int,input().strip())] for _ in range(N)]
visited=[ [False]*M for _ in range(N)]

def isRange(y,x):
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

#벽을 부수는 개수(break_cnt)를 기준으로 우선순위 큐
def bfs():
    q.put((0,0,0))
    visited[0][0]=True
    while q:
        break_cnt, y, x=q.get()

        #도착점 도달
        if (y==N-1) and (x==M-1):
            return break_cnt
            
        for i in range(4):
            nexty, nextx=y+dy[i], x+dx[i]
            if isRange(nexty, nextx):
                #아직 방문하지 않았다면
                if not visited[nexty][nextx]:
                    if MAP[nexty][nextx]==0:
                        q.put((break_cnt,nexty, nextx))
                    else:
                        q.put((break_cnt+1,nexty,nextx))
                    visited[nexty][nextx]=True        

result=bfs()
print(result)
