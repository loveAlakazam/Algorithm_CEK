import sys
input= sys.stdin.readline

def solution():
    N,K= map(int,input().split())
    A=sorted(list(map(int,input().split())))
    print(A[K-1])

if __name__=='__main__':
    solution()
