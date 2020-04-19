def binary_search(target,N, A):
    left, right=0, N-1
    while (left<=right):
        mid=(left+right)//2
        if A[mid]==target:
            return 1
        elif A[mid]>target:
            right=mid-1
        elif A[mid]<target:
            left=mid+1
    return 0

def sol():
    N=int(input())
    A=list(map(int,input().split()))
    M=int(input())
    B=list(map(int,input().split()))
    A.sort()
    for b in B:
        print(binary_search(b,N, A))
        
if __name__=='__main__':
    sol()
