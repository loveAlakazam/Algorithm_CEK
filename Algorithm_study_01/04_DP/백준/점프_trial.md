# 실패1
- 이유: 무한으로 (3,3)이 append됨
- 코드
```python
import sys

def main():
    N=int(sys.stdin.readline())
    arr=[]
    visited=[]
    for _ in range(N):
        arr.append( list(map(int, sys.stdin.readline().split())))
        visited.append( [0]*N)
    print(arr)
    print(visited)
    #방문한 노드
    order=[]
    order.append((0,0)) #원점 시작
    # 현재 좌표가 N-1보다 작거나 같은가?
    while order[0][0]<N-1 or order[0][1]<N-1:
        r, c=order.pop(0) #맨앞의 점을 pop한다
        visited[r][c]+=1
        tmp=arr[r][c]
        go_right= c+tmp
        go_down= r+tmp
        if go_right<N:
            order.append((r, go_right))
        if go_down<N:
            order.append((go_down, c))
        print(order)
    print(visited[N-1][N-1])
        
if __name__=='__main__':
    main()
```

<hr>

# 실패2
- 이유: 채점결과 메모리 초과로 판정.
- 코드
```python
from collections import deque
import sys

def main():
    N=int(sys.stdin.readline())
    A=[list(x for x in map(int, sys.stdin.readline().split())) for _ in range(N)]

    d=deque()
    d.append((0,0))
    result=0
    
    while len(d)>0:
        row, col= d.popleft()
        if (row!=N-1 or col!=N-1):
            now_val= A[row][col]
            go_right= col+now_val
            go_down= row+now_val
            if go_right<N:
                d.append((row, go_right))

            if go_down<N:
                d.append((go_down, col))
                
        else:#row=N-1, col=N-1
            result+=1
            
    print(result)
if __name__=="__main__":
    main()
```

<HR>

# 성공
- 1890_점프02.py 코드
- board[r][c]=0 으로 초기화 (0<=r<N, 0<=c<N)
- jump=A[r][c]
- r<N-1 and r+jump<N -> board[r+jump][c]+= board[r][c]
- c<N-1 and c+jump<N -> board[r][c+jump]+= board[r][c]
- 코드
```python
    # -*- coding: utf-8 -*-
# 참고: https://it-and-life.tistory.com/136
# 1890. 점프
import sys
        
def main():
    N=int(sys.stdin.readline())
    A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    board=[ [0]*N for _ in range(N)]
    print(A)
    
    board[0][0]=1
    for r in range(N):
        for c in range(N):
            jump=A[r][c]
            if r<N-1 and r+jump<N:
                board[r+jump][c]+=board[r][c]
              
            if c<N-1 and c+jump<N:
                board[r][c+jump]+=board[r][c]
    print(board[N-1][N-1])

if __name__=="__main__":
    main()
```

