import sys
from copy import deepcopy
input=sys.stdin.readline

#N: 지도 세로크기, M:지도 가로크기
# y,x : 각각 북쪽으로부터, 서쪽으로부터 떨어진 칸의수.
# K: 명령의 개수
N,M,y,x,K=map(int, input().strip().split())

#지도
MAP=[]
for _ in range(N):
    MAP.append([*map(int, input().strip().split())])

#명령
# 동:1/ 서:2/ 북:3/ 남:4
ORDER=[*map(int, input().strip().split())]
dy=[0,0,-1,1]
dx=[1,-1,0,0]

#윗면:0, 북쪽방향:1, 동쪽방향:2, 서쪽방향:3, 남쪽방향:4, 바닥면:5
DICE=[0]*6

def isRange(y,x):
    if (y>=0 and y<N) and (x>=0 and x<M):
        return True
    return False

def roll(order):
    tmp=deepcopy(DICE)
    if order==1: #동쪽으로 굴린다. (남북은 그대로)
        tmp[0]=DICE[3]
        tmp[2]=DICE[0]
        tmp[3]=DICE[5]
        tmp[5]=DICE[2]
        
    elif order==2:#서쪽으로 굴린다.(남북은 그대로)
        tmp[0]=DICE[2]
        tmp[2]=DICE[5]
        tmp[3]=DICE[0]
        tmp[5]=DICE[3]
    
    elif order==3: #북쪽으로 굴린다.(동서는 그대로)
        tmp[0]=DICE[4]
        tmp[1]=DICE[0]
        tmp[4]=DICE[5]
        tmp[5]=DICE[1]
        
    else:#남쪽으로 굴린다.(동서는 그대로)
        tmp[0]=DICE[1]
        tmp[1]=DICE[5]
        tmp[4]=DICE[0]
        tmp[5]=DICE[4]
    return tmp
    

#주사위의 위치
nowy, nowx= y,x
upper=DICE[0]
for i in range(K):
    #현재 지도위치의 값이 0인가?
    if MAP[nowy][nowx]==0:
        MAP[nowy][nowx]=DICE[5] #아랫면의 수를 현재지도위치에 복사
    else:
        DICE[5]=MAP[nowy][nowx]
        MAP[nowy][nowx]=0
        
    nexty=nowy+dy[ORDER[i]-1]
    nextx=nowx+dx[ORDER[i]-1]
    #주사위의 (지도에서의) 위치가 적절한가?
    if isRange(nexty, nextx):
        nowy=nexty
        nowx=nextx
        
        #주사위를 굴린다.
        DICE=roll(ORDER[i])
        
        #이동한 칸에 쓰여있는 수가 0인가?
        if MAP[nowy][nowx]==0:
            #주사위 바닥면에 쓰여있는 수가 칸에 복사된다.
            MAP[nowy][nowx]=DICE[5]
        #이동한 칸에 쓰여있는 수가 0이 아니라면
        else:
            #칸에 쓰여있는 수가 주사위 바닥면으로 복사되고
            #칸에 쓰여있는 수는 0이된다.
            DICE[5]=MAP[nowy][nowx]
            MAP[nowy][nowx]=0
        #주사위 윗면에 쓰여있는 수를 출력한다.
        print(DICE[0])


