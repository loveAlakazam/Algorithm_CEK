import sys
input=sys.stdin.readline
def solution():
    T=int(input().strip())
    for _ in range(T):
        n=int(input().strip())
        result=[0]*11
        result[1]=1
        result[2]=2
        result[3]=4
        if n<11:
            for i in range(4,n+1):
                result[i]=result[i-1]+result[i-2]+result[i-3]
            print(result[n])

if __name__=='__main__':
    solution()
