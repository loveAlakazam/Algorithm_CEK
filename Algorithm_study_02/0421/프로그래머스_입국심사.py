def solution(n, times):
    left, right=1, max(times)*n
    
    while left<=right:
        mid=int((left+right)//2)
        
        cnt=0
        for time in times:
            cnt+=int(mid//time)
        
        if cnt>=n:
            right=mid-1
        else:
            left=mid+1
    return left
