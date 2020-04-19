import sys
input=sys.stdin.readline
        
def solution():
    T=int(input())
    for _ in range(T):
        n= int(input())
        cnt0=[0]*(n+1)
        cnt1=[0]*(n+1)
        cnt0[0]=1
        if n>0: #n>=1이어야한다.
            cnt1[1]=1
        for i in range(2,n+1):
            cnt0[i]=cnt0[i-1]+cnt0[i-2]
            cnt1[i]=cnt1[i-1]+cnt1[i-2]
        print(cnt0[n],cnt1[n])
if __name__=='__main__':
    solution()
