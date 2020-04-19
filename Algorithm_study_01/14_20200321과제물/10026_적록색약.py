import sys
from collections import deque
input= sys.stdin.readline
q=deque()

#입력#
N= int(input())
MAP=[ [*input().strip()] for _ in range(N)]

NORMAL_AREA={'R':0, 'G':0, 'B':0} #정상인
NOT_GREEN={'R': 0, 'B':0}#적록색약
visited=[ [False]*N for _ in range(N) ]

#상/하/좌/우
dy=(-1,1,0,0)
dx=(0,0,-1,1)

def isRange(y,x):
    if (y>=0 and y<N) and (x>=0 and x<N):
        return True
    return False

def bfs(flag):
    not_green=flag
    while q:
        cury, curx=q.popleft()
        #현재 위치 아직 방문안한 상태라면
        if not visited[cury][curx]:
            visited[cury][curx]=True #방문
            for i in range(4):
                nexty=cury+dy[i]
                nextx=curx+dx[i]
                
                #현위치의 상/하/좌/우 가 적절한 위치인가?
                if isRange(nexty, nextx):
                    #정상인#
                    if not not_green:
                        #현위치의 상/하/좌/우가 현위치값과 동일하고, 아직 방문안한 상태인가?
                        if (MAP[nexty][nextx]==MAP[cury][curx]) and (not visited[nexty][nextx]):
                            q.append((nexty, nextx))
                            
                    #적록색약#
                    else:
                        #현위치값이 R/G이고, 현위치의 상/하/좌/우 값이 R/G이고 아직 방문 안한 상태인가?
                        if (MAP[cury][curx]=='R' or MAP[cury][curx]=='G') and (MAP[nexty][nextx]=='R' or MAP[nexty][nextx]=='G') and (not visited[nexty][nextx]):
                            q.append((nexty, nextx))

                        #현재위치값이 B이고, 현위치의 상/하/좌/우 값이 B라면
                        elif (MAP[cury][curx]=='B') and (MAP[nexty][nextx]==MAP[cury][curx]) and (not visited[nexty][nextx]):
                            q.append((nexty, nextx))
                        
#정상인#
for y in range(N):
    for x in range(N):
        #아직 방문하지 않은 상태라면
        if not visited[y][x]:
            #BFS 연산을하여 구역개수 카운트
            q.append((y,x))
            bfs(flag=False)
            #MAP[y][x]값( R/G/B) 에 따른 NORMAL_AREA 카운트
            NORMAL_AREA[MAP[y][x]]+=1

#적록색약#
visited=[ [False]*N for _ in range(N) ]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            q.append((y,x))
            bfs(flag=True)
            if MAP[y][x]=='R' or MAP[y][x]=='G':
                NOT_GREEN['R']+=1
            else:#'B'
                NOT_GREEN[MAP[y][x]]+=1

#정상인 사람은 세구역 모두 본다.
#적록색약인 사람은 초록색 구역을 제외한 나머지만 본다.
print('{} {}'.format(sum(NORMAL_AREA.values()),  sum(NOT_GREEN.values())))

