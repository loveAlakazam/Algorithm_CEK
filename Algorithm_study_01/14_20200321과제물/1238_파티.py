import sys
from copy import deepcopy
input=sys.stdin.readline

# N: 학생수/  M: 도로개수 / X: 파티장소
N, M, X = map(int, input().strip().split())

# 가중치 집합 초기화
weight=[ [float('inf') if i!=j else 0 for j in range(N+1)] for i in range(N+1)]
for _ in range(M):
    start, end, time= map(int, input().strip().split())
    weight[start][end]=time

visited=None
distance=None

def choose():
    global distance, N, visited
    min_val= float('inf')
    min_pos=0
    for i in range(1,N+1):
        if (min_val> distance[i]) and (not visited[i]):
            min_val=distance[i]
            min_pos=i
    return min_pos
      

# 최단거리를 구한다.
def shortest_path(start): #start:시작정점, n: 정점개수
    global N,X, visited, weight, distance
    #초기화
    visited=[False]*(N+1)
    distance= deepcopy(weight[start]) #시작정점에 해당하는 가중치 복사.
    visited[start]=True #시작정점 방문표시

    #시작정점과 연결된 노드중 가장 짧은 거리를 갖는 노드(u)를 찾는다.
    #시작정점을 제외한 나머지 노드를 탐색해야하므로 최대 N-1회 반복한다. 
    for i in range(N-1):
        u=choose()
        visited[u]=True #연결노드 방문
        for w in range(1,N+1):
            if not visited[w]: #노드 w가 아직 방문하지 않은 상태라면
                if (distance[u]+weight[u][w]<distance[w]):
                    distance[w]=distance[u]+weight[u][w]
    

def main():
    global X,N, distance, visited, weight
    # cost_time: 각 학생이 파티장소까지 이동하고, 집으로 돌아오는데 걸린시간
    cost_time={}
    cost_time[X]=0

    #파티장->각 학생의 집
    shortest_path(X)
    for i in range(1,N+1):
        if i!=X:
            cost_time[i]=distance[i]

    #학생집-> 파티장
    #학생집을 출발점으로 하게되면 n번의 반복을 할 수있지만
    #방향만 바꿔준다면, 반복을 안해도 된다.
    # 즉, 파티장소(X)를 출발점으로해서 학생의 집에 도달할 수 있다.
    #weight[1][2]=4 , weight[2][1]=1 을 swapping
    visited= [[False]*(N+1) for _ in range(N+1)]
    for y in range(1,(N+1)):
        for x in range(1,(N+1)):
            if (not visited[y][x]):
                visited[y][x]=True
                visited[x][y]=True
                weight[y][x], weight[x][y]= weight[x][y], weight[y][x] 
    
    shortest_path(X)
    for i in range(1,N+1):
        if i!=X:
            cost_time[i]+=distance[i]
    print(max(cost_time.values()))

if __name__=='__main__':
    main()
