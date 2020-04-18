import sys
from copy import deepcopy
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

dy=(-1,1,0,0)
dx=(0,0,-1,1)
max_alpha=0

def dfs(cury, curx, cnt):
    global MAP,R,C, max_alpha, visited

    max_alpha=max(max_alpha, cnt)
    for i in range(4):
        nexty=cury+dy[i]
        nextx=curx+dx[i]
        if (nexty>=0 and nexty<R) and (nextx>=0 and nextx<C):
            if not visited[ord(MAP[nexty][nextx])-ord('A')]:
                visited[ord(MAP[nexty][nextx])-ord('A')]=True
                dfs(nexty, nextx, cnt+1)
                visited[ord(MAP[nexty][nextx])-ord('A')]=False
                
R,C= map(int, input().strip().split())
MAP=[ [*input().strip()] for _ in range(R)]

visited=[False]*26
visited[ord(MAP[0][0])-ord('A')]=True
dfs(0,0,1)
print(max_alpha)
