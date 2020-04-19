import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=0
ans=0
isStop=False

#동일한 패턴이 존재하는가?
def isSatisfy(n, nums):
    for i in range(1, (n//2)+1):        
        if nums[n-(i*2):n-i] == nums[n-i:]:
            return False
    return True


def backtracking(n, nums):
    global N, ans, isStop
    if isStop:
        return
    
    if n==N:
        ans= int(nums)
        isStop=True
        
    else:
        for i in range(1,4):
            #똑같은 패턴이 존재하지 않은 숫자인가?
            if (isSatisfy(n+1, nums+str(i))):
                backtracking(n+1, nums+str(i))
                    
def main():
    global N, ans
    N=int(input())
    backtracking(n=1, nums='1')
    print(ans)

if __name__=='__main__':
    main()
