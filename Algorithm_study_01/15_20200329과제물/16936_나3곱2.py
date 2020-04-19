import sys
input=sys.stdin.readline
#입력#
N=int(input())
B=[*map(int, input().strip().split())]

def dfs(x, cnt, A):
    #연산횟수가  N-1회라면
    if cnt==N-1:
        return A
    
    #x가 B에 있는가?
    if x in B:
        #x가 3에 나눠떨어지는 수인가?->나3연산
        if x%3==0:
            #x//3값이 B에 있다면
            if (x//3) in B:
                return dfs(x//3, cnt+1, A+[x//3])
        # x*2값이 B에 있다면
        if (x*2) in B:
            return dfs(x*2, cnt+1, A+[x*2]) #곱2연산

for i in range(N):
    x=dfs(B[i], 0, [B[i]])
    if not (x is None):
        print(' '.join(map(str,x)))
        break
    
    
