import sys
input=sys.stdin.readline

#집의 수
N=int(input())

#집
HOUSE=[ [*map(int, input().strip().split())] for _ in range(N)]

#현재N의 색깔과 N-1집 색깔은 서로 같지 않으므로, 점화식을 세우면
# DP[N][0]= HOUSE[N][0]+ min(DP[N-1][1], DP[N-1][2])
# DP[N][1]= HOUSE[N][1]+ min(DP[N-1][0], DP[N-1][2])
# DP[N][2]= HOUSE[N][2]+ min(DP[N-1][0], DP[N-1][1])
#=>모든 집을 칠하는 비용의 가장 최솟값: min(DP[N][0], DP[N][1], DP[N][2])
DP= [ [0]*3 for _ in range(N)]
for i in range(N):
    if i==0:
        DP[i]=HOUSE[0]
    else:
        DP[i][0]=HOUSE[i][0]+min(DP[i-1][1], DP[i-1][2])
        DP[i][1]=HOUSE[i][1]+min(DP[i-1][0], DP[i-1][2])
        DP[i][2]=HOUSE[i][2]+min(DP[i-1][0], DP[i-1][1])

result=min(DP[N-1])
print(result)
