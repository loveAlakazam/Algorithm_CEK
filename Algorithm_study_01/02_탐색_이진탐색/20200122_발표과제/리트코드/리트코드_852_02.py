class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left,right=0, len(A)-1
        while left<right:
            mid=(left+right)//2
            if A[mid]<A[mid+1]: #오른쪽이 크다면 left를 mid+1인덱스로 한다.
                left=mid+1
            else:
                right=mid
        return left #left<right조건이 만족하지 않을 때 left값을 리턴
    
    #ex) A=[ 0, 1, 2, 0 ]
    # step 01
    # left=0 , right=3 -> mid=1
    # A[mid]=1, A[mid+1]=2 -> A[mid]<A[mid+1] -> left=mid+1
    # 
    # step 02
    # left=2, right=3 -> mid=2
    # A[mid]=2, A[mid+1]=0 -> right를 mid로 한다. -> right=mid
    # 
    # step 03
    # left=2, right=2 -> while-loop 조건에 맞지 않음 -> left:2 
    # A[2] =2 (최댓값)
