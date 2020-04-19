import sys
from collections import deque
input=sys.stdin.readline
q=deque()
MAP=None
visited=None
w,h=0,0

dy=[-1,-1,-1, 0, 0, 1, 1, 1]
dx=[-1,0, 1,  -1, 1, -1, 0, 1]

def isRange(y,x):
    global w, h
    if (y>=0 and y<h) and (x>=0 and x<w):
        return True
    return False
    

def bfs(y,x):
    global visited, MAP
    q.append((y,x)) #큐에 넣는다.
    while q:
        y,x=q.popleft()
        #아직 방문 안했는가?
        if not visited[y][x]:
            visited[y][x]=True
            for i in range(8):
                nexty=y+dy[i]
                nextx=x+dx[i]
                if isRange(nexty, nextx):
                    #아직방문하지 않은 상태이고, 1인가?
                    if (not visited[nexty][nextx]) and (MAP[nexty][nextx]==1):
                        q.append((nexty,nextx))

def solution():
    global visited, MAP, w, h
    result=0
    for y in range(h-1, -1, -1):
        for x in range(w-1, -1, -1):
            if (MAP[y][x]==1) and (not visited[y][x]):
                bfs(y,x) #탐색
                result+=1
    return result
    
def main():
    global visited, MAP, w,h
    ISLANDS=[]
    while True:
        #w: 지도의 너비/  h: 지도의 높이
        w,h= map(int, input().strip().split())

        #입력 종료
        if (w==0) or (h==0):
            break

        MAP=[] #지도 입력
        visited=[ [False]*w for _ in range(h)] #방문리스트 초기화
        for y in range(h):
            MAP.append([*map(int, input().strip().split())])
        ISLANDS.append(solution())

    #출력
    for i in ISLANDS:
        print(i)

if __name__=='__main__':
    main()
    
