import sys
from itertools import combinations as comb
input=sys.stdin.readline   

N=int(input().strip())
S=[ [*map(int, input().strip().split())] for _ in range(N)]
members=[*range(1,N+1)]

# member중 절반으로 나눠서
# 동일 인원수의 스타트팀과 링크팀을 나누는 케이스
START=[*comb(members, N//2)]
LINK=[ [*filter(lambda x: x not in start  ,members)] for start in START]

min_diff=float('inf')
for starts, links in zip(START, LINK):
    start_ability=0
    link_ability=0
    for i in range( N//2 -1):
        for j in range(i+1, N//2):
            start_ability+=(S[starts[i]-1][starts[j]-1]+S[starts[j]-1][starts[i]-1])
            link_ability+=(S[links[i]-1][links[j]-1]+S[links[j]-1][links[i]-1])
    min_diff=min(min_diff, abs(start_ability-link_ability))

print(min_diff)
