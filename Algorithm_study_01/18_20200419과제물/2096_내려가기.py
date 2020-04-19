import sys
from copy import deepcopy
input=sys.stdin.readline

N=int(input())
MAP=[ [*map(int, input().strip().split())]for _ in range(N)]

DP_MAX=[ [0]*3 for _ in range(2)]
DP_MIN=[ [0]*3 for _ in range(2)]

DP_MAX[0][0]=DP_MIN[0][0]=MAP[0][0]
DP_MAX[0][1]=DP_MIN[0][1]=MAP[0][1]
DP_MAX[0][2]=DP_MIN[0][2]=MAP[0][2]
    
for now in range(1,N):
    DP_MAX[1][0]=max(DP_MAX[0][0], DP_MAX[0][1])+MAP[now][0]
    DP_MAX[1][1]=max(DP_MAX[0][0], DP_MAX[0][1], DP_MAX[0][2])+MAP[now][1]
    DP_MAX[1][2]=max(DP_MAX[0][1], DP_MAX[0][2])+MAP[now][2]

    DP_MIN[1][0]=min(DP_MIN[0][0], DP_MIN[0][1])+MAP[now][0]
    DP_MIN[1][1]=min(DP_MIN[0][0], DP_MIN[0][1], DP_MIN[0][2])+MAP[now][1]
    DP_MIN[1][2]=min(DP_MIN[0][1], DP_MIN[0][2])+MAP[now][2]

    DP_MAX[0][0]=DP_MAX[1][0]
    DP_MAX[0][1]=DP_MAX[1][1]
    DP_MAX[0][2]=DP_MAX[1][2]

    DP_MIN[0][0]=DP_MIN[1][0]
    DP_MIN[0][1]=DP_MIN[1][1]
    DP_MIN[0][2]=DP_MIN[1][2]
    
print(max(DP_MAX[0]), min(DP_MIN[0]))

    
