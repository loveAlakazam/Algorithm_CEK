# -*- coding : utf-8 -*-
import sys

class Kevin:
    def __init__(self, N):
        self.N= N #유저수(노드)
        self.visited=None
        self.connection=[ [] for _ in range(N)] #연결관계
        self.kevin_result=[] #각 노드의 케빈베이컨 수를 나타내는 리스트
        self.q=[] #bfs에 사용될 큐

    def bfs(self, start):
        #시작노드 :start , 끝노드: end
        #시작노드에서 끝노드까지 도달하는데 간선의 개수를 추가한다
        tmp=[0]* self.N
        self.q.append((start, 0)) #큐에 추가 (시작노드, 간선수)
        while self.q:
            val, cnt= self.q.pop(0)
            #현재노드가 방문하지 않은 상태라면
            if self.visited[val-1] is False:
                self.visited[val-1]=True #노드 방문
                tmp[val-1]=cnt

                #크기가 val인 노드와 연결된 노드를 큐에 추가하고
                #단, 연결된 노드는 방문하지 않은 상태이다.
                #간선수 카운트
                for x in self.connection[val-1]:
                    if self.visited[x-1] is False:
                        self.q.append((x, cnt+1))
        self.kevin_result.append((start, sum(tmp)))
                    

    def find_kevin(self):
        for start in range(1, self.N+1):
            #방문리스트 초기화
            self.visited=[False]* self.N
            self.bfs(start)

        #먼저 노드의 케빈수[1]을 기준으로 오름차순정렬
        #동일한경우 start[0]을 기준으로 오름차순정렬
        self.kevin_result=sorted(self.kevin_result, key=lambda x:(x[1], x[0]) )
        print(self.kevin_result[0][0])
        

def main():
    N, M= map(int, sys.stdin.readline().split())
    
    k=Kevin(N) #Kevin 객체생성
    #관계 리스트 만들기
    for m in range(M):
        f1, f2= map(int, sys.stdin.readline().split())
        k.connection[f1-1].append(f2)
        k.connection[f2-1].append(f1)

    k.find_kevin()
    


if __name__=='__main__':
    main()
