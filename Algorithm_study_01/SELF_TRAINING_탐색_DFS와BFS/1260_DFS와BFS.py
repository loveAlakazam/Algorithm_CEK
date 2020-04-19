# -*- coding: utf-8 -*-
import sys

class Graph:
    def __init__(self,N,M,V):
        self.N= N #노드의 개수
        self.M=M #간선의 개수
        self.V=V #시작정점
        #인접리스트 만들기
        self.connection=[[] for _ in range(N)]

        #방문리스트 만들기
        self.visited= [False]*N

        #DFS탐색 결과
        self.dfs_result=[]
        
        #BFS탐색 결과
        self.q=[]
        self.bfs_result=[]

    def connection_sort(self):
        #연결리스트를 오름차순으로 sort한다
        for i in range(self.N):
            self.connection[i]=sorted(self.connection[i])

    def DFS(self, v):
        #방문을 했는지/안했는지 확인한다
        if self.visited[v-1] is False:
            #노드 방문
            self.dfs_result.append(v)
            self.visited[v-1]=True

            #현재노드 v와 연결된 노드 탐색
            for x in self.connection[v-1]:
                self.DFS(x)
                
    def BFS(self, v):
        #현재노드 v를 방문했는지 확인
        if self.visited[v-1] is False:
            #큐에 넣는다
            self.q.append(v)
            
            while self.q: #큐에 노드가 들어있다면
                #now: q에서 pop한 노드를 의미한다
                now=self.q.pop(0)

                #노드 now의 방문상태(visited[now-1]) 확인
                if self.visited[now-1] is False:
                    #노드 now를 방문한다
                    self.bfs_result.append(now)
                    self.visited[now-1]=True

                    #now와 연결된 노드x를 큐에 넣는다
                    for x in self.connection[now-1]:
                        self.q.append(x)


def main():
    #N,M,V를 입력받는다
    N,M,V = map(int, sys.stdin.readline().split())
    
    #그래프 객체를 만든다
    g=Graph(N,M,V)

    #간선을 확인한다
    for _ in range(M):
        #입력받고
        v1, v2= map(int, sys.stdin.readline().split())
        #connection[v1-1]에 v2를 추가
        #connection[v2-1]에 v1을 추가
        g.connection[v1-1].append(v2)
        g.connection[v2-1].append(v1)

    #간선 연결된 노드를 오름차순순으로 한다
    g.connection_sort()
    g.DFS(V) #DFS탐색
    print(' '.join(map(str, g.dfs_result)))
    
    #방문리스트를 초기화하고
    g.visited=[False]*N
    g.BFS(V) #BFS탐색
    print(' '.join(map(str,g.bfs_result)))

if __name__=='__main__':
    main()
