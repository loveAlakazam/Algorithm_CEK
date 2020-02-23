def isRange(y,x, n, m):
    if(y>=0 and y<n) and (x>=0 and x<m):
        return True
    return False

def solution(m, n, puddles):
    maps=[[0 for x in range(m)] for y in range(n)]#지도초기화
    dp=[[0 for x in range(m)] for y in range(n)] #경로 초기화
    
    for px, py in puddles:#물웅덩이 위치의 maps값 -1
        maps[py-1][px-1]=-1
    
    
    dy=(-1,0) #위, 왼쪽
    dx=(0,-1)
    dp[0][0]=1
    for y in range(n):
        for x in range(m):
            if maps[y][x]!=-1:
                for i in range(2):
                    prevy=dy[i]+y
                    prevx=dx[i]+x
                    if isRange(prevy,prevx,n,m):
                        if maps[prevy][prevx]!=-1:
                            dp[y][x]+=dp[prevy][prevx]
                dp[y][x]%=1000000007
                
    answer=dp[n-1][m-1]
    return answer
