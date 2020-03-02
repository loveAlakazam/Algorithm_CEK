# -*- coding: utf-8 -*-
import sys

class Maze:
    def __init__(self, N, M):
        self.N= N  #행
        self.M= M #열
        self.maze= [] #maze
        self.visited=[[False]*M for _ in range(N)] #방문리스트
        #우선순위
        # 아래, 오른쪽, 위, 왼쪽
        self.directions=[(1,0), (0,1), (-1,0), (0,-1)]
        
        self.q=[]
        
    def isRange(self, y,x):#현재위치가 N*M 배열의 원소에 적합한지 확인
        if (y<0) or (y>=self.N) or (x<0) or (x>=self.M):
            return False
        return True

    def bfs(self):
        while self.q:
            cury, curx, now_cnt =self.q.pop(0)# 현재위치, '1'개수 출력
            
            #현재위치가 방문하지 않은 상태라면..
            if self.visited[cury][curx] is False:
                self.visited[cury][curx]=True #방문을 한다
                
                #만일 현재위치가 (N-1, M-1)이라면
                if (cury==self.N-1) and (curx==self.M-1):
                    return now_cnt

                #현재위치의 오른쪽/아래/위/왼쪽 순으로 살펴본다
                for dy, dx in self.directions:
                    nexty= cury+dy
                    nextx= curx+dx
                    
                    #N*M 배열안의 원소인가?
                    if self.isRange(nexty, nextx):
                        # 다음 노드의 값이 '1'이고 아직 방문하지 않은 상태인가?
                        if (self.maze[nexty][nextx]=='1') and (self.visited[nexty][nextx] is False):
                            self.q.append((nexty, nextx, now_cnt+1)) #큐에 추가

def main():
    #행/열 구하기
    N,M = map(int, sys.stdin.readline().split())
    #maze객체 생성
    maze=Maze(N,M)
    
    #미로 지도 그리기
    for y in range(N):
        tmp=list(sys.stdin.readline().strip())
        maze.maze.append(tmp)

    #미로찾기 탐색(bfs)
    #시작점: (0,0) , 도착점: (N-1, M-1)
    #시작점 큐에 넣기
    maze.q.append((0,0,1))
    result=maze.bfs()
    print(result)
    
            
if __name__=='__main__':
    main()
