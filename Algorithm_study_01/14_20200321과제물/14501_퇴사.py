import sys
from copy import deepcopy
input=sys.stdin.readline

MAX_DAY=17
T=[0]*(MAX_DAY)
P= [0]*(MAX_DAY)
DP=[0]*MAX_DAY

#입력
N=int(input()) 
for i in range(1,N+1):
    T[i], P[i]= map(int, input().strip().split())

MAX=0
#   N번째날에 일한다면, N+1번째 날에 돈을 받는다.
for i in range(1,N+1):
    #i번째날에 일을 한경우-> (i+1)번째날에 돈을 받는다.
    if i+T[i]<=N+1:
        DP[i+T[i]]=max(DP[i+T[i]], DP[i]+P[i])
        MAX= max(MAX, DP[i+T[i]])
        
    #i번째날에 일을 안한 경우-> (i+1)번째날에 돈을 받지 않는다.
    DP[i+1]=max(DP[i+1], DP[i])
    MAX=max(MAX, DP[i+1])

print(MAX)
