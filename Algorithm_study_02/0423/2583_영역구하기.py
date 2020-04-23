import sys
from collections import deque
q=deque()
input=sys.stdin.readline
dy=(-1,1,0,0)
dx=(0,0,-1,1)

def bfs(y,x):
    global MAP,M,N, visited
    q.append((y,x))
    area=0
    while q:
        cury, curx = q.popleft()
        #현위치가 아직 방문안한 상태라면
        if not visited[cury][curx]:
            #방문횟수 +1
            area+=1
            visited[cury][curx]=True

            #현위치의 상하좌우 탐색
            for i in range(4):
                nexty=cury+dy[i]
                nextx=curx+dx[i]
                if (nexty>=0 and nexty<M) and (nextx>=0 and nextx<N):
                    if (MAP[nexty][nextx]==0) and (not visited[nexty][nextx]):
                        q.append((nexty, nextx))
    return area


if __name__=='__main__':
    M,N,K=map(int, input().strip().split())
    MAP=[[0]*N for _ in range(M)]
    
    visited=[[False]*N for _ in range(M)]
    for _ in range(K):
        #아래 꼭짓점좌표, 위꼭짓점 좌표
        dlx, dly, urx, ury= map(int, input().strip().split())
        for y in range(dly, ury):
            for x in range(dlx, urx):
                MAP[y][x]=1

    A=[]
    for y in range(M):
        for x in range(N):
            if (MAP[y][x]==0) and (not visited[y][x]):
                A.append(bfs(y,x))
            
    print(len(A))
    print(' '.join(map(str, sorted(A))))
