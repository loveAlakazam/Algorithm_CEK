import sys
def main():
    N=int(sys.stdin.readline())
    A=list(map(int, sys.stdin.readline().split()))
    
    dp=[0]*N
    dp[0]=A[0]
    max_val= float('-inf')
    for i in range(1,N):
        dp[i]= max(dp[i-1]+A[i], A[i])
        max_val= max(max_val, dp[i])
    max_val= max(max_val, A[0])
    print(max_val)
if __name__=='__main__':
    main()
