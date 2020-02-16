# 1. 시도1 (실패)
### DFS와 BFS를 같이활용
- DFS: 연결된 빙산 그룹 개수 카운트
- BFS: 1년후 빙산을 구할 때 사용
- (BFS)빙산변화 -> (DFS)그룹카운트 -> 빙산개수가 1보다클때 
- 결과: 6%에서 시간초과
- 코드
```python
# -*- coding: utf-8 -*-
import sys
N,M= map(int, sys.stdin.readline().split())
ice=[list(map(int, sys.stdin.readline().split())) for _ in range(N)] #ice: 초기 빙산 배열

#현재빙산의 상/하/좌/우 에 위치한 빙산
d=[(-1,0), (1,0), (0,-1), (0,1)]

#현위치가 적절한지 확인해주는 함수
def isRange(nexty, nextx):
    global N,M
    if (nexty>=0 and nexty<N) and (nextx>=0 and nextx<M):
        return True
    return False

def dfs(y,x, visited):
    #방문을한다
    visited[y][x]=True

    #상하 좌우 살펴본다
    for dy, dx in d:
        nexty= y+dy
        nextx= x+dx

        if isRange(nexty, nextx): #0~N-1행, 0~M-1열 위치에 속하는지
            #(nexty, nextx)는 visited=False이며
            #0이 아닌 값을 갖는다면
            if (visited[nexty][nextx] is False) and (ice[nexty][nextx]!=0):
                dfs(nexty, nextx, visited)

def count_group(ice):
    cnt=0
    visited=[[False]*M for _ in range(N)] #빙산 카운트 방문리스트
    for y in range(N):
        for x in range(M):
            if ice[y][x]==0:
                continue
            else: #빙산
                #방문했는지 확인
                if visited[y][x] is False:
                    cnt+=1
                    dfs(y,x,visited)
    return cnt
                    

def main():
    global ice
    time=0 #time: 걸리는 시간(출력값)
    #빙산그룹이 1개면 반복문을  종료하지 않는다.
    finish=False
    while not finish:
        next_year=[[0]*M for _ in range(N)] #1년후 빙산배열
        visited=[[False]*M for _ in range(N)] #방문리스트
        q=[]

        for y in range(N):
            for x in range(M):
                if ice[y][x]==0:
                    continue
                #0이아닌 빙산이고
                #만일 방문을하지 않았따면
                elif visited[y][x] is False:
                    q.append((y,x)) #현재 좌표를 큐에 넣는다. 
                    while q:
                        cury,curx=q.pop(0) #현재위치
                        visited[cury][curx]=True #방문
                        water_cnt=0 #주변 물 개수
                        next_year[cury][curx]= ice[cury][curx] #현재값 임시저장
                        
                        for dy, dx in d: #현위치의 상/하/좌/우
                            nexty=cury+dy
                            nextx=curx+dx

                            #N행M열의 원소인지확인
                            if isRange(nexty, nextx):
                                if ice[nexty][nextx]==0: #물이라면
                                    water_cnt+=1
                                else:#큐에추가
                                    #큐에 추가하기전에 먼저 방문하지 않은 노드인지를 확인
                                    if visited[nexty][nextx] is False:
                                        q.append((nexty, nextx))
                                    
                        
                        #그런데 water_cnt가 현재값보다 더 크거나 같으면 0으로한다.
                        if water_cnt>=next_year[cury][curx]:
                            next_year[cury][curx]=0
                        else:#water_cnt<next_year[cury][curx]
                            next_year[cury][curx]-=water_cnt


        #1년후 빙산 -> 빙산의 그룹개수 카운트(group_cnt)
        time+=1
        ice=next_year
        group_cnt=count_group(ice)
        #만일 빙산그룹이 2개이상이면 반복문을 종료한다.
        if group_cnt>1:
            finish=True
    return time

if __name__=='__main__':
    result=main()
    print(result)
```

<hr>

# 2. 시도2 (실패)
### BFS에서 둘다 활용
- BFS: 연결된 빙산 그룹 개수 카운트
- BFS: 1년후 빙산을 구할 때 사용
- BFS 빙산변화 & 그룹카운트 -> 빙산그룹 개수가 1보다 크면 루프문 종료
- 결과: 6%에서 시간초과 동일
- 코드 
```python
import sys
N,M= map(int, sys.stdin.readline().split())
ice=[list(map(int, sys.stdin.readline().split())) for _ in range(N)] #ice: 초기 빙산 배열

#현재빙산의 상/하/좌/우 에 위치한 빙산
d=[(-1,0), (1,0), (0,-1), (0,1)]

#현위치가 적절한지 확인해주는 함수
def isRange(nexty, nextx):
    global N,M
    if (nexty>=0 and nexty<N) and (nextx>=0 and nextx<M):
        return True
    return False

def main():
    global ice
    time=0 #time: 걸리는 시간(출력값)  
    while True:
        next_year=[[0]*M for _ in range(N)] #1년후 빙산배열
        visited=[[False]*M for _ in range(N)] #방문리스트
        q=[]
        group_cnt=0 #빙산그룹 개수

        for y in range(N):
            for x in range(M):
                if (ice[y][x]==0) or(visited[y][x] is True):
                    continue
                
                #0이아닌 빙산이고
                #만일 방문을하지 않았따면
                elif visited[y][x] is False:
                    group_cnt+=1 #시작점 원소카운트
                    q.append((y,x)) #현재 좌표를 큐에 넣는다.
                    while q:
                        cury,curx=q.pop(0) #현재위치
                        visited[cury][curx]=True #방문
                        water_cnt=0 #주변 물 개수
                        next_year[cury][curx]= ice[cury][curx] #현재값 임시저장
                        
                        for dy, dx in d: #현위치의 상/하/좌/우
                            nexty=cury+dy
                            nextx=curx+dx

                            #N행M열의 원소인지확인
                            if isRange(nexty, nextx):
                                if ice[nexty][nextx]==0: #물이라면
                                    water_cnt+=1
                                else:#큐에추가
                                    #큐에 추가하기전에 먼저 방문하지 않은 노드인지를 확인
                                    if visited[nexty][nextx] is False:
                                        q.append((nexty, nextx))
                                    
                        #그런데 water_cnt가 현재값보다 더 크거나 같으면 0으로한다.
                        if water_cnt>=next_year[cury][curx]:
                            next_year[cury][curx]=0
                        else:#water_cnt<next_year[cury][curx]
                            next_year[cury][curx]-=water_cnt

        #만일 빙산그룹이 2개이상이면 반복문을 종료한다.
        if group_cnt>1:
            break
        time+=1
        ice=next_year
    return time

if __name__=='__main__':
    result=main()
    print(result)
```

<hr>

# 시도3 
### Pypy3로 하면 성공 1020ms..; 
### 반면, python3로 하면  시간초과로 실패

- BFS
- 결과: 12%에서 실패
- 코드
```python
import sys
N,M= map(int, sys.stdin.readline().split())
ice=[list(map(int, sys.stdin.readline().split())) for _ in range(N)] #ice: 초기 빙산 배열
visited=[ [False]*M for _ in range(N)]#방문리스트

#현재빙산의 상/하/좌/우 에 위치한 빙산
d=[(-1,0), (1,0), (0,-1), (0,1)]

def melt(y,x):
    global ice
    melt_cnt=0
    for dy, dx in d:
        nexty= y+dy
        nextx= x+dx

        if ice[nexty][nextx]==0:
            melt_cnt+=1
    return melt_cnt

def BFS(y,x):
    global ice
    global visited
    q=[]
    
    q.append((y,x)) #좌표를 큐에 넣는다
    visited[y][x]=True
    while q:
        print(q,'\n')
        cury, curx= q.pop(0)
        for dy, dx in d: #현위치의 상하좌우
            nexty= dy+cury
            nextx= dx+curx

            #방문을 안한 상태라면 큐에 넣는다.
            #그리고 물이아닌 빙산인 경우만 해당한다.
            if (ice[nexty][nextx]!=0) and(visited[nexty][nextx] is False):
                #방문을 한다
                visited[nexty][nextx]=True
                q.append((nexty, nextx))
        
def solution():
    global ice
    global N,M
    global visited

    year=0
    while True:
        print('\n\nyear: ', year)
        group_cnt=0 #빙산그룹 카운트
        ice_copy=[[0]*M for _ in range(N)]
        for y in range(1,N):
            for x in range(1,M):
                #방문하지 않았고, 0이 아니라면.
                if (ice[y][x]!=0) and (visited[y][x] is False):
                    group_cnt+=1
                    BFS(y,x)#BFS를 실행한다.
                    
        if group_cnt>1:
            return year
        if group_cnt==0:
            return 0

        #ice_copy를 다음 ice로 갱신
        for y in range(1,N-1):
            for x in range(1,M-1):
                if ice[y][x]!=0:
                    ice_copy[y][x]= ice[y][x]-melt(y,x)
                    if ice_copy[y][x]<0:
                        ice_copy[y][x]=0              
        ice=ice_copy
        visited=[ [False]*M for _ in range(N)]#방문리스트 다시 초기화
        year+=1
    
def main():
    print(solution())

if __name__=='__main__':
    main()

```


<hr>

# 시도4 (실패)
- 런타임에러가 뜬다. (너무 늦어서 해결을 못했음..ㅠ)
- DFS를 이용
- 코드
```python
import sys
N,M= map(int, sys.stdin.readline().split())
ice=[list(map(int, sys.stdin.readline().split())) for _ in range(N)] #ice: 초기 빙산 배열

#현재빙산의 상/하/좌/우 에 위치한 빙산
d=[(-1,0), (1,0), (0,-1), (0,1)]

def melt(y,x):
    global ice
    melt_cnt=0
    for dy, dx in d:
        nexty= y+dy
        nextx= x+dx

        if ice[nexty][nextx]==0:
            melt_cnt+=1
    return melt_cnt

# 빙산을 방문한다.
def DFS(y,x, visited):
    global ice
    visited[y][x]=True #방문을한다

    for dy, dx in d:
        nexty= dy+y
        nextx= dx+x
        #물이 아니고, 방문을 안햇따면.
        if (ice[nexty][nextx]>0) and (visited[nexty][nextx] is False):
            DFS(nexty, nextx,visited)

#dfs를 이용하여 연결된 빙산을 찾는다
def isconnect():
    global N,M
    visited=[ [False]*M for _ in range(N)]
    cnt=0
    for y in range(N):
        for x in range(M):
            if (ice[y][x]>0) and (visited[y][x] is False):
                DFS(y,x,visited)#깊이탐색하고
                cnt+=1 #카운트
    return cnt

def solution():
    global ice
    global N,M
    year=0
    while True:
        ice_copy=[[0]*M for _ in range(N)]
        #빙산그룹 카운트
        group_cnt=isconnect()
        if group_cnt>1:
            return year
        if group_cnt==0:
            return 0

        #ice_copy를 다음 ice로 갱신
        for y in range(0,N):
            for x in range(0,M):
                if ice[y][x]!=0:
                    ice_copy[y][x]= max(0,ice[y][x]-melt(y,x))            
        ice=ice_copy
        year+=1
    
def main():
    print(solution())

if __name__=='__main__':
    main()
```
