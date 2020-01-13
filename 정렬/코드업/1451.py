import sys, io
input=sys.stdin.readline

def solution():
    N=int(input())
    arr=[]
    for n in range(N):
        arr.append(int(input()))
    for n in sorted(arr):
        print(n)
    
if __name__=='__main__':
    solution()
