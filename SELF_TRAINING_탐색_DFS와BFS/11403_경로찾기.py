# -*- coding: utf-8 -*-
import sys
N=int(sys.stdin.readline())
connect=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans=[ ['0']*N for _ in range(N)]
visited=None

def dfs(start, end):
    global N, connect, visited
    if connect[start][end]==1:
        return True

    if not visited[start]:#아직 방문 안한 상태라면
        visited[start]=True #방문을한다

        #연결된 노드 탐색
        for x in range(N):
            #start와 연결된 노드 x, 방문아직 안한상태
            if (connect[start][x]==1) and (not visited[x]):
                if dfs(start=x, end=end):
                    return True
    
    
def main():
    global N, connect, ans, visited
    for i in range(N):
        for j in range(N):
            visited=[False]*N #초기화
            if dfs(start=i, end=j):
                ans[i][j]='1'

    for x in ans:
        print(' '.join(x))

if __name__=='__main__':
    main()
