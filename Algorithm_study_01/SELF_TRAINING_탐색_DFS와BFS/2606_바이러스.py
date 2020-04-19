# -*- coding: utf-8 -*-
import sys
from collections import deque
q=deque()
N,E= 0,0
visited=None
connected=None

def bfs():
    global visited, connected
    get_virus=[] #1번노드 빼고걸림
    result=0
    
    while q:
        now=q.popleft()
        
        #현재노드가 아직 방문하지 않았다면
        if not visited[now-1]:
            visited[now-1]=True #now 번 컴퓨터 방문
        
            if now!=1: #1번이아닌 다른 컴퓨터가 바이러스에 걸렸다면-> 리스트에 추가한다.
                get_virus.append(now)

            # now와 연결된 노드리스트에서
            #아직 방문하지 않은 상태라면 큐에 추가
            for c in connected[now-1]:
                if not visited[c-1]:
                    q.append(c)
                    
    if len(get_virus)>0:
        result=len(get_virus)
    return result
    

def main():
    global N,E, visited, connected
    N= int(sys.stdin.readline()) #컴퓨터 수(노드수)
    E= int(sys.stdin.readline()) #간선의 개수
    visited=[False]*N #방문리스트
    connected= [ [] for _ in range(N)] #연결된 노드 리스트
    
    for _ in range(E):
        c1, c2= map(int, sys.stdin.readline().split())
        connected[c1-1].append(c2)
        connected[c2-1].append(c1)

    q.append(1) #1번컴퓨터가 웜바이러스에 걸렸다
    print(bfs())

if __name__=='__main__':
    main()
