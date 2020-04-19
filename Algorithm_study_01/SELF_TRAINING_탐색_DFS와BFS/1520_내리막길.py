import sys
sys.setrecursionlimit(10**6)

#M: 세로(행), N:가로(열) 
M,N=map(int, sys.stdin.readline().split())
maps=[ list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp=[ [-1]*N for _ in range(M)] #방문리스트

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def isRange(y,x):
    global N,M
    if(y>=0 and y<M) and(x>=0 and x<N):
        return True
    return False

def dfs(y,x):
    global dp, cnt, maps
    
    #현위치가 (0,0)인가?-> 1을 리턴
    if (y==0) and (x==0):
        return 1
     
    #아직 방문하지 않은 상태인가?
    if dp[y][x]==-1:
        dp[y][x]=0 #방문한다
        now=maps[y][x]
        
        #상/하/좌/우를 살펴보고
        #현위치의 값보다 작은곳으로 이동.
        for i in range(4):
            nexty= y+dy[i]
            nextx= x+dx[i]

            #적절한위치?
            if isRange(nexty, nextx):
                #현위치값보다 큰경우라면
                if (maps[nexty][nextx]>now) :
                    dp[y][x]+= dfs(nexty, nextx)
                    
    #더이상 상하좌우에 움직일수 없다면 -> backtracking한다.
    #현재까지의 경로개수를 리턴.
    return dp[y][x]

def main():
    global maps, M,N
    print(dfs(M-1,N-1))

if __name__=='__main__':
    main()
