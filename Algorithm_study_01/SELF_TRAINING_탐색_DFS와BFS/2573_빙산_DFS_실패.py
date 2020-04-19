# -*- coding: utf-8 -*-
# 2573. 빙산 (DFS)
import sys
from copy import deepcopy

class Ice:
    def __init__(self,N,M):
        self.N=N
        self.M=M
        self.arr=[]
        self.directions=[(1,0), (0,1), (-1,0), (0,-1)]#아래/오른쪽/위/왼쪽
        self.visited=None

    def isRange(self, y, x):
        if (y>=0 and y<self.N) and (x>=0 and x<self.M):
            return True
        return False
    
    def dfs(self, y, x):
        if not self.visited[y][x]: #아직 방문하지 않은 상태라면
            self.visited[y][x]=True #현재위치 (y,x)를 방문한다

            #상/하/좌/우 중, 아직 방문하지 않은 빙산을 찾는다.
            for dy, dx in self.directions:
                nexty=y+dy
                nextx=x+dx
                #적절한 범위에 있는지 확인
                if self.isRange(nexty, nextx):
                    if (self.arr[nexty][nextx]!=0) and (not self.visited[nexty][nextx]) :
                        self.dfs(nexty, nextx)
                    
    def iceburgCount(self): #빙산그룹개수를 카운트한다
        cnt=0
        for y in range(self.N):
            for x in range(self.M):
                if (self.arr[y][x]!=0) and (not self.visited[y][x]):
                    cnt+=1
                    self.dfs(y,x)
        return cnt

    def melt(self): #빙산을 녹여, 1년후 빙산의 모습을 나타낸다.
        #self.arr의 복사본을 만든다
        tmp=deepcopy(self.arr)
        for y in range(self.N):
            for x in range(self.M):
                if tmp[y][x]!=0:
                    for dy, dx in self.directions:
                        nexty=dy+y
                        nextx=dx+x
                        #적절한 범위에 있고, 0값을 갖는다면
                        if  self.isRange(nexty,nextx) and (self.arr[nexty][nextx]==0):
                            tmp[y][x]-=1
                    tmp[y][x]=max(tmp[y][x], 0)
        self.arr=tmp
        
            
def main():
    N,M= map(int, sys.stdin.readline().split())
    ice=Ice(N,M) #Ice객체 생성

    #배열 만들기
    for _ in range(N):
        ice.arr.append(list(map(int, sys.stdin.readline().split())))
        
    time=0
    while True: #빙산그룹개수를 카운트한다.
        ice.visited=[[False]*M for _ in range(N)] #방문리스트 초기화
        group_cnt=ice.iceburgCount()
        if group_cnt>=2:
            break
        if group_cnt==0:
            time=0
            break
        ice.melt() #빙산을 녹인다.
        time+=1#1년이 지났다.
    print(time)
    
if __name__=='__main__':
    main()
