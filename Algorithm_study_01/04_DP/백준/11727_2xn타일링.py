import sys
def main():
    n=int(sys.stdin.readline())
    dp=[0]*(n+1)
    dp[1]=1
    if n>=2:
        dp[2]=3
        
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]*2

    print(dp[n]%10007)
    
if __name__=='__main__':
    main()
