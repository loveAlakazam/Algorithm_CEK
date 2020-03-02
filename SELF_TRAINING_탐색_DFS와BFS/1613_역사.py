import sys
from collections import deque

n,k=0,0
q= deque()
visited=None# 방문리스트
c=None#사건 전후관계를 인접리스트로 나타냄.

def bfs(num):
    global visited, c,n
    target=num
    while q:
        now=q.popleft()     
        #아직 방문하지 않은 상태인가?
        if not visited[now-1]:
            visited[now-1]=True
            
            #c[target][now]!=-1이라면
            if c[target-1][now-1]!=-1:
                c[target-1][now-1]=-1
                c[now-1][target-1]=1

            #아직방문 안한상태이고, now 이전사건인 사건(h)들을 구한다.
            #c[now-1][h-1]=-1
            for h in range(1,n+1):
                if (not visited[h-1]) and (c[now-1][h-1]==-1):
                    q.append(h)

def main():
    global n,k, c, visited
    
    # n: 사건의 개수
    # k: 전후관계의개수
    n,k = map(int, sys.stdin.readline().split())

    #k개의 알고있는 사건의 전후관계를 입력한다.
    c=[ [0]*n for _ in range(n)] 
    for _ in range(k):
        before, after= map(int, sys.stdin.readline().split())
        c[before-1][after-1]=-1 # before->after
        c[after-1][before-1]=1 #after<-before

    for h in range(1,n+1):
        #방문리스트 초기화
        visited=[False]*n
        
        #h와 연결된 사건들중 h이후의 사건들을 큐에 추가 (c[h-1][x-1]==-1)
        for x in range(1,n+1):
            if c[h-1][x-1]==-1:
                q.append(x)
        #bfs실행
        bfs(num=h)

    # s: 사건 전후 관계를 알고 싶은 사건 쌍의 개수
    s= int(sys.stdin.readline())
    for _ in range(s):
        left, right= map(int, sys.stdin.readline().split())
        print(c[left-1][right-1])
        
if __name__=='__main__':
    main()
