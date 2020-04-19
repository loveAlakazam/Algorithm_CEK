import sys
from copy import deepcopy
input=sys.stdin.readline

#입력#
cogs=[]
cogs_clockwise=[0]*4 #초기화 
for _ in range(4):
    cogs.append([*map(int,input().strip())])

K=int(input())

#톱니 K번 회전#
for _ in range(K):
    target, clockwise= map(int, input().strip().split())
    cogs_clockwise[target-1]=clockwise

    #(1) target의 왼쪽부터확인
    #now가 0번이면 (1번톱니) 더이상 왼쪽은 존재하지 않는다.
    for now in range(target-1, 0, -1):
        #현재톱니는 회전중인가?
        if abs(cogs_clockwise[now])==1:
            #현재톱니의 6번째값과, 왼쪽톱니의 2번째값이 같은가?-> 왼쪽톱니 정지
            if cogs[now][6]==cogs[now-1][2]:
                cogs_clockwise[now-1]=0

            #다르다면-> 왼쪽톱니는 현재 톱니의 반대방향으로 회전
            else:
                cogs_clockwise[now-1]=(-1)*cogs_clockwise[now]

        #현재 톱니가 회전하지 않으면, 왼쪽톱니도 회전하지 않는다.
        else:
            cogs_clockwise[now-1]=0

    #(2) target의 오른쪽확인
    #now가 3번이면 더이상 오른쪽은 존재하지 않는다.
    for now in range(target-1, 3):
        #현재 톱니는 회전중인가?
        if abs(cogs_clockwise[now])==1:
            #현재톱니의 2번째값과 오른쪽톱니의 6번째 값이 같은가?->오른쪽 톱니 정지
            if cogs[now][2]==cogs[now+1][6]:
                cogs_clockwise[now+1]=0
            else:
                cogs_clockwise[now+1]=(-1)*cogs_clockwise[now]
        else:
            cogs_clockwise[now+1]=0
        
    #(3) 톱니회전
    for i in range(4):
        if cogs_clockwise[i]==1: #시계방향
            tmp=deepcopy(cogs[i])
            cogs[i]=tmp[-1:]+tmp[:-1]
            
        elif cogs_clockwise[i]==-1:#반시계방향
            tmp=deepcopy(cogs[i])
            cogs[i]=tmp[1:]+[tmp[0]]
    
#K번회전후 톱니상태 결과
result=0
for i in range(4):
    #12시방향의 cogs[i][0]이 1이라면 => 2**i만큼 더한다.
    if cogs[i][0]==1:
        result+=2**i

print(result)
