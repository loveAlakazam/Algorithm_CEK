import sys
def main():
    N=int(sys.stdin.readline())
    points=[0]*(N+1)
    dp=[0]*(N+1)
    
    for i in range(1,N+1):
        points[i]=int(sys.stdin.readline())
        
    dp[1]=points[1]
    for n in range(2,N+1):
        if n>=3:
            dp[n]=points[n]+max(dp[n-3]+points[n-1],  dp[n-2])
        else:
            dp[n]=points[n]+max(dp[n-1], dp[n-2])
    print(dp[N])
    
if __name__=='__main__':
    main()
