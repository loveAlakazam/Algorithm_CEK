# -*- coding: utf-8 -*-
import sys
from collections import deque
input= sys.stdin.readline

q=deque()
n,m=0,0
connections=None
visited=None

def bfs():
    global visited, connections
    invite_cnt=0 #초대횟수
    set_sg=set(connections[0])|set([1]) #상근이와 상근이 친구들
    
    while q:
        now= q.popleft()
        
        #아직 방문하지 않았다면
        if not visited[now-1]:
            visited[now-1]=True #방문

            #now의 친구들중.. 상근이와 친구들(set_sg)와 겹치는 것이 있는가?
            #now의 친구들중에서 상근이(1)가 있거나, 상근이의친구가 있는가?
            set_now=set(connections[now-1])
            isSGFriend= set_now & set_sg
            if len(isSGFriend)>0:
                invite_cnt+=1
                
            for f in connections[now-1]:
                if not visited[f-1]:
                    q.append(f)

    return invite_cnt
    
def main():
    global n,m, connections, visited
    n=int(input()) #상근이 동기수(노드개수)
    m=int(input()) #연결리스트 길이(간선개수)
    connections=[ [] for _ in range(n)]
    
    #친구 연결관계 개수
    for _ in range(m):
        a,b= map(int, input().split())
        connections[a-1].append(b)
        connections[b-1].append(a)

    #상근이(1)를 제외한 나머지는 방문을 안한상태로 둔다.
    visited= [ False if num>1 else True for num in range(1,n+1)] #방문리스트

    #상근이 친구를 큐에 먼저 넣는다.
    for f in connections[0]:
        q.append(f)     
    print(bfs())

if __name__=='__main__':
    main()
        
        
    
