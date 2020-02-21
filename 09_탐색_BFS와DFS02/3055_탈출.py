# -*- coding: utf-8 -*-
import sys
from collections import deque

R,C= map(int, sys.stdin.readline().split())
maps=[ list(sys.stdin.readline().strip()) for _ in range(R)]

water_visited=[[False]*C for _ in range(R)] #물웅덩이 방문여부
visited=[[False]*C for _ in range(R)] #고슴도치의 방문여부

start_y, start_x =0,0 #S위치 초기화
q=deque() #덱

#상하좌우를 나타내는 좌표
dy=[-1,1,0,0]
dx=[0,0,-1,1]

#R*C 배열의 원소인지 확인
def isRange(y,x):
    global R,C
    if (y>=0 and y<R) and (x>=0 and x<C):
        return True
    return False

def bfs():
    global maps, water_visited, visited

    result=0 #고슴도치가 D에 도착하는데 걸리는 시간
    while q: #큐가 비어있지 않았다면
        y, x, time= q.popleft()
        
        #고슴도치가 D에 도착했다면-> break하고 time을 리턴한다.
        if maps[y][x]=='D':
            result=time
            break
        
        #현위치가 물웅덩이이고, 아직 퍼지지 않은 상태인가?
        elif (maps[y][x]=='*') and (not water_visited[y][x]):
            water_visited[y][x]=True #물웅덩이 방문
            for i in range(4): #상하좌우 인접한 물웅덩이 확장
                nxt_wy= y+dy[i]
                nxt_wx= x+dx[i]
                
                if isRange(nxt_wy, nxt_wx): #적절한 위치인가?
                    #만일 인접한 곳이 '.'이고, 아직 물이 접하지 않은 상태라면.
                    if ((maps[nxt_wy][nxt_wx]=='.') or(maps[nxt_wy][nxt_wx]=='S')) and (not water_visited[nxt_wy][nxt_wx]):
                        maps[nxt_wy][nxt_wx]='*' #'.'에서 '*'로 바꾼다.
                        q.append((nxt_wy, nxt_wx, time+1)) #큐에 추가. 그리고 시간(time)을 +1한다.
            
        #현위치가  'S'이거나'.' 이고, 아직 고슴도치가 방문하지 않은 상태라면
        elif  ((maps[y][x]=='S') or (maps[y][x]=='.'))  and(not visited[y][x]):
            visited[y][x]=True #고슴도치 방문
            for i in range(4): #상하좌우 인접한 도로를 구한다.
                nxt_y=y+dy[i]
                nxt_x=x+dx[i]
                
                if isRange(nxt_y, nxt_x): #적절한 위치인가?
                    #만일 인접한 곳이 '.'이거나 'D'이고, 고슴도치가 방문하지 않은 상태라면
                    if ((maps[nxt_y][nxt_x]=='.') or(maps[nxt_y][nxt_x]=='D')) and (not visited[nxt_y][nxt_x]):
                        q.append((nxt_y, nxt_x, time+1))

    #큐가 비어져서 빠져나갔을때 현위치가 D인지 아닌지를 확인
    if maps[y][x]!='D':#아직못빠져나감-> KAKTUS를 리턴
        return 'KAKTUS'
    return result

def main():
    global R,C, maps
    global start_y, start_x
    waters=[]
    #1. 0초일때 고슴도치의 위치, 도착점위치, 물웅덩이(*)위치를 먼저 찾는다.
    #먼저 고슴도치의 시작점부터 큐에 넣는다
    #물웅덩이(*)인 경우에는 waters라는 리스트에 넣어놓은 뒤에 차례대로 큐에 넣는다..
    for y in range(R):
        for x in range(C):
            if (maps[y][x]=='S'): #시작점 설정
                start_y, start_x= y,x
                #고슴도치 시작위치를 큐에넣는다.
                q.append((start_y, start_x, 0))
                
            elif(maps[y][x]=='D'):#도착점 설정
                end_y, end_x= y,x
                
            elif(maps[y][x]=='*'):#물웅덩이 위치-> 큐에 넣는다.
                waters.append((y, x, 0)) #값, 행위치, 열위치, 시간=0
                
    #탐색이 끝나면 q에 물웅덩이들의 위치를 넣는다.
    for water in waters:
        q.append(water)

    #2. BFS탐색
    #물웅덩이 인접부분인 .은 *이된다 (단, D와 X는 물웅덩이가 될 수 없다)
    time=bfs()
    print(time)
 
if __name__=='__main__':
    main()
