import sys
from collections import deque

N=0
MAP=[]
visited=None
outter=None

q0=deque() #섬번호 부여
q1= deque() #바다가 인접한 섬위치를 저장하는 역할.-> 섬을 확장.

# 현위치의 상/하/좌/우
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def isRange(y,x):
    global N
    if (y>=0 and y<N) and (x>=0 and x<N):
        return True
    return False

def bfs_labeling(cury, curx, label_number):
    global MAP, visited
    #매개변수를 큐에 추가한다.
    q0.append((cury, curx, label_number))
    
    while q0:
        y, x,  label= q0.popleft()
        if not visited[y][x]:
            visited[y][x]=True #방문
            MAP[y][x]=label #섬번호 부여

            water_cnt=0 #주변에 바다가 접해있는지 확인.
            #현위치의 상/하/좌/우가 바다가 아닌 육지(1)라면
            for i in range(4):
                nexty, nextx= y+dy[i], x+dx[i]
                
                if isRange(nexty, nextx):
                    #현위치의 주변에 바다가 있는지 확인해야한다.
                    if MAP[nexty][nextx]==0:
                        water_cnt+=1
                        
                    #방문을 하지 않았고, 육지라면.-> 육지번호를 부여
                    if (not visited[nexty][nextx]) and (MAP[nexty][nextx]==1):
                        q0.append((nexty, nextx, label))
            if water_cnt>0:
                #주변에 바다가 1개이상이라면있다면, 바다와 인접한 위치이다.
                #0은 다른섬이 나올때까지의 경로를 카운트한다.
                q1.append((y,x,label,0))

def bfs(island_cnt):#island_cnt: 섬개수
    global visited, MAP
    #최소거리를 구한다.
    dist=[0]*(island_cnt)
    
    #q1은 바다와 인접한 섬의 위치이다. (이미 방문한 상태)
    #점점 섬번호로 확장해나간다. 그 위치의 주변이 서로다른 섬번호라면
    #현위치섬번호가 간거리 + 다른섬번호가 간거리 합으로 리턴한다.
    while q1:
        y, x, label, d=q1.popleft()
        MAP[y][x]=label
        dist[label-1]=d

        #현위치 주변에 아직 방문하지 않은 바다가 있는지 탐색한다. 그리고 dist[label]을 카운트한다.
        #만일 바다가 아닌 다른 섬번호라면 dist[현재섬번호]+dist[인접다른섬번호] 를 리턴
        for i in range(4):
            nexty, nextx= y+dy[i], x+dx[i]
            if isRange(nexty, nextx):
                #바다가 아닌 다른 섬번호이면.
                if (MAP[nexty][nextx]>0) and (MAP[nexty][nextx]!=label):
                    return dist[label-1]+dist[MAP[nexty][nextx]-1]
                
                elif (not visited[nexty][nextx]) and (MAP[nexty][nextx]==0):
                    visited[nexty][nextx]=True #방문을 한다.
                    q1.append((nexty, nextx, label, d+1))

               
def main():
    global N, MAP, visited
    N=int(sys.stdin.readline()) #지도의 크기 입력
    visited=[[False]*N for _ in range(N)]  #방문리스트 입력
    
    for _ in range(N): #지도그리기
        MAP.append( list( map(int, sys.stdin.readline().split()) ) )

    #지도번호 라벨링
    label_number=1
    island_cnt=0 #섬개수 카운트
    for y in range(N):
        for x in range(N):
            if (MAP[y][x]!=0) and (not visited[y][x]):
                bfs_labeling(y,x, label_number)
                island_cnt+=1#섬개수 카운트
                label_number+=1
    print(bfs(island_cnt)) #bfs실행.
    #큐를 비운다.
    q0.clear()
    q1.clear()
       
      
if __name__=='__main__':
    main()
