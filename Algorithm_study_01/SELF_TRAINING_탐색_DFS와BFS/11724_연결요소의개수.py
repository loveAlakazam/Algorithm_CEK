# -*- coding: utf-8 -*-
#11724. 연결요소의 개수
import sys
sys.setrecursionlimit(10**6)
class Graph:
    def __init__(self, N):
        self.N=N
        self.relation=[ [] for _ in range(N)] #관계리스트
        self.visited=[False]*N #방문리스트

    def dfs(self, v):
        if not self.visited[v-1]:
            self.visited[v-1]=True #노드방문
            
            #노드 v와 연결된 노드를 찾는다.
            #연결되 노드는 방문하지 않은 상태여야한다.
            for x in self.relation[v-1]:
                if not self.visited[x-1]:
                    self.dfs(x)
        
def main():
    N,M= map(int, sys.stdin.readline().split())
    cnt=0
    if (M>=0) and (M<=N*(N-1)//2):
        g=Graph(N) #그래프 객체 생성    
        for _ in range(M):#그래프 vertex간의 연결
            u,v=map(int, sys.stdin.readline().split())
            g.relation[u-1].append(v)
            g.relation[v-1].append(u)

        #노드  v와 연결된 노드들 탐색
        #아직 v가 탐색되지 않은 상태라면 cnt증가
        for v in range(1,N+1):
            if not g.visited[v-1]:
                g.dfs(v)
                cnt+=1
    print(cnt)

if __name__=='__main__':
    main()
