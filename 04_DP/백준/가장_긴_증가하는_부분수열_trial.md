# 시도1 (실패: 틀렸습니다)
```python
# -*- coding: utf-8 -*-
import sys

def main():
    N=int(sys.stdin.readline())
    A=list( map(int, sys.stdin.readline().strip().split()) )
    print(N, A)
    dp=[0]*N
    for now, a  in enumerate(A):
        if now>0:
            if A[now]>A[now-1]:
                dp[now]=dp[now-1]+1
            else:
                dp[now]=dp[now-1]
        else:#now==0
            dp[now]=1
    print(dp[N-1])
    
if __name__=='__main__':
    main()
```

<hr>

#시도2
