# -*- coding: utf-8 -*-
import sys

class Friends:
    def __init__(self, N):
        self.N= N
        self.visited=[False]* N #방문리스트 초기화
        self.connection=[ [] for _ in range(N)] #노드 관계리스트
        self.answer=0
        self.flag=False

    def dfs(self, start, cnt):
        # 현재 간선의개수가 4개인가?
        if cnt==4:
            self.flag=True
            return

        #start노드 방문
        self.visited[start]=True
        
        #start와 연결된 노드를 찾는다.
        for x in self.connection[start]:
            #그 노드가 아직 방문되지 않았다면 dfs로 재탐색
            if self.visited[x] is False:
                self.dfs(x, cnt+1)
                self.visited[x]=False
  
def main():
    N,M = map(int, sys.stdin.readline().split())
    f= Friends(N) #객체 Friends생성
    
    for _ in range(M): 
        p1, p2= map(int, sys.stdin.readline().split())
        f.connection[p1].append(p2) #노드 p1의 관계리스트에 p2추가
        f.connection[p2].append(p1) #노드 p2의 관계리스트에 p1추가

    #친구관계(간선의 개수)가 4개이상이 될때까지 dfs 탐색
    for i in range(N):
        f.dfs(start=i, cnt=0)
        f.visited[i]=False
        if f.flag:
            f.answer=1
            break
    print(f.answer)

if __name__=='__main__':
    main()
