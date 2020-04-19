import sys
from collections import deque
input=sys.stdin.readline
q=deque()

#상/하/좌/우
dy=(-1,1,0,0)
dx=(0,0,-1,1)

#입력
N,L,R=map(int, input().strip().split())
A=[]
for _ in range(N):
    A.append([*map(int, input().strip().split())])

def isRange(y,x):
    global N
    if (y>=0 and y<N) and (x>=0 and x<N):
        return True
    return False

def bfs(y,x):
    global L,R,A,N, visited
    unions=[]
    q.append((y,x))
    while q:
        y,x=q.popleft()
        if not visited[y][x]:
            visited[y][x]=True
            unions.append((y,x,A[y][x]))
            for i in range(4):
                nexty, nextx=y+dy[i], x+dx[i]
                if isRange(nexty, nextx):
                    if (L<=abs(A[nexty][nextx]-A[y][x])<=R) and (not visited[nexty][nextx]):
                        q.append((nexty,nextx))
           
    union_sum=0
    for i in range(len(unions)):
        union_sum+=unions[i][2]

    union_sum=int(union_sum/len(unions))
    for i in range(len(unions)):
        A[unions[i][0]][unions[i][1]]=union_sum


def solution():
    global N,L,R,A, visited
    #나라가 1개밖에 없으므로 인구이동할 필요가 없다.
    if N==1:
        return 0
    
    result=0
    while True:
        visited=[[False]*N for _ in range(N)]
        keep_loop=False
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    cnt=0
                    for i in range(4):
                        nexty=y+dy[i]
                        nextx=x+dx[i]
                        if isRange(nexty, nextx):
                            if L<=abs(A[nexty][nextx]-A[y][x])<=R:
                                cnt+=1
                                break
                    #상/하/좌/우 중  현재위치의 인구수차이가 L~R사이가 최소 한개라도 있다면.
                    if cnt>0:
                        bfs(y,x)
                        keep_loop=True
       
        if not keep_loop:
            break
        result+=1
    return result
    
def main():
    print(solution())
    
if __name__=='__main__':
    main()
