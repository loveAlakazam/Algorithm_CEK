# -*- coding: utf-8 -*-
#7544ms.. 메모리 149344KB
#정말 비효율적이야... ㅠㅠㅠ....

import sys
R,C=0,0
board=None
visited=None
unique_alpha=[0]*26 #알파벳 사용여부 확인 리스트
cnt=1 #처음 시작점 카운트
ans=1#처음 시작점 카운트

#방향: 오른쪽, 왼쪽, 아래, 위
dy=[-1,1,0,0]
dx=[0,0,-1,1]

#R행*C열에 적절한 행렬인가?
def isRange(y,x):
    global R,C
    if (y>=0 and y<R) and (x>=0 and x<C):
        return True
    return False


def dfs(y,x, cnt):
    global visited, board, unique_alpha, ans
    
    # 방문이 안되어있고, 현재알파벳이 사용되지 않았다면?
    if (not visited[y][x]): 
        visited[y][x]=True
        now=board[y][x]
        unique_alpha[now]=1 #알파벳 사용
        
        #상하좌우 알파벳
        for i in range(4):
            nexty=y+dy[i]
            nextx=x+dx[i]

            #적절한 위치에 있는가?
            if isRange(nexty, nextx):
                next=board[nexty][nextx]
                #아직 사용되지 않은 알파벳 && 방문하지 않은 상태
                if(not visited[nexty][nextx]) and(unique_alpha[next]==0):
                    dfs(nexty,nextx, cnt+1)

        ans=max(cnt, ans)
        unique_alpha[now]=0
        visited[y][x]=False
        cnt-=1
        
        
def main():
    global R,C, board,  visited, unique_alpha
    board=[] #board초기화
    R,C= map(int, sys.stdin.readline().split()) #R: 행(세로), C:열(가로)
    
    for _ in range(R):#board에 원소 넣기
        board.append(list(map(lambda x: ord(x)-ord('A'), sys.stdin.readline().strip())))

    visited=[ [False]*C  for _ in range(R)] #방문리스트 초기화
    dfs(0,0,1)
    print(ans)
    
if __name__=='__main__':
    main()
