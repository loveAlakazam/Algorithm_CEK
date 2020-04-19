# -*- coding: utf-8 -*-
import sys
from collections import deque
connections=None
visited=None
q= deque()

def bfs():
    global visited, connections
    edge_cnt=0 # start와 연결된 간선의 개수
    while q:
        p, cnt=q.popleft()
        # p(1,2,3,..,N)가 아직 방문이 안한 상태인가?
        if not visited[p-1]:
            visited[p-1]=True
            edge_cnt+=cnt#edge_cnt에 cnt를 더한다.
            
            # p와 연결된 노드x가 아직 방문하지 않은 상태인가?
            for x in connections[p-1]:
                if not visited[x-1]:
                    q.append((x, cnt+1)) #큐에 추가
                    
    #큐가 비어있으면 edge_cnt를 리턴
    return edge_cnt    

def main():
    global connections, visited
    
    # N: 유저의수 (노드개수)
    # M: 친구관계수 (노드간 연결관계)
    N, M= map(int, sys.stdin.readline().split())

    #각 노드별 친구관계리스트 입력
    connections=[[] for _ in range(N)] #N명의 연결관계 리스트

    # f1과 f2는 친구이므로
    # f1의 친구관계 리스트에 f2를 추가
    # 반대로, f2의 친구관계 리스트에 f1을 추가
    for _ in range(M):
        f1, f2= map(int, sys.stdin.readline().split())
        connections[f1-1].append(f2)
        connections[f2-1].append(f1)

    kevin_nums={} #각 노드별 케빈베이컨 수를 딕셔너리로 나타냄.
    # BFS를 이용하여, 각 노드별 케빈베이컨 수를 구한다.
    for start in range(1,N+1):
        visited=[False]*N #방문리스트 visited 초기화
        q.append((start,0)) #start: 1,2,3,...,N
        result=bfs() # start에서 시작해서 각 노드에 도착한 간선수의 합
        kevin_nums[start]=result
        
    # kevin_nums의 value를 기준으로 오름차순 정렬
    # 동일한 value를 가질때 key값(사람번호)이 작은걸  우선시한다.
    kevin_nums=sorted(kevin_nums.items() , key=lambda x: (x[1], x[0]))
    print(kevin_nums[0][0])
    
if __name__=='__main__':
    main()
