import sys
from collections import deque
input=sys.stdin.readline
q=deque()

N, M= map(int, input().split())
MAP=[   [*input().strip()] for _ in range(N)]
max_distance=0

dy=(-1,1,0,0)
dx=(0,0,-1,1)

def isRange(y,x):
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

def bfs(y,x,cnt):
    max_dist=0
    visited=[[False]*M for _ in range(N)]
    q.append((y,x,cnt))
    while q:
        y,x, cnt=q.popleft()
        if not visited[y][x]:
            visited[y][x]=True
            
            if max_dist<cnt:
                max_dist=cnt
            for i in range(4):
                nexty=y+dy[i]
                nextx=x+dx[i]
                if isRange(nexty, nextx):
                    if (not visited[nexty][nextx]) and (MAP[nexty][nextx]=='L'):
                        q.append((nexty, nextx, cnt+1))
    return max_dist #멀리떨어진 거리 리턴 
        
result=0
for y in range(N):
    for x in range(M):
        if MAP[y][x]=='L':
            result=max(result, bfs(y,x,0))
print(result)
