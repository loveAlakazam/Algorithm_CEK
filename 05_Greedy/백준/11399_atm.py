import sys

def main():
    N=int(sys.stdin.readline())
    P=list(map(int, sys.stdin.readline().split()))
    P=sorted(P)
    print(P)
    result=0
    times=[0]*N
    for i in range(N):
        if i==0:
            times[i]=P[i]
        else:# i>0
            times[i]=times[i-1]+P[i]
        result+=times[i]
    print(times)
    print(result)
    
if __name__=="__main__":
    main()
