# 1613. 역사

## 시도1 (실패)

- 방법: 인접리스트와 DFS를 활용
- 결과: 4% 정도에서 시간초과 뜸.
- 코드
```python
# -*- coding: utf-8 -*-
import sys
class History:
    def __init__(self, n):
        self.n= n
        self.connect=[ [0]*n for _ in range(n)] #인접리스트
        self.visited=None #방문리스트

    def dfs(self, start, target):
        if self.connect[start][target]!=0:
            return self.connect[start][target]

        for x in range(self.n):
            if (x!=start) and (x!=target):
                if (not self.visited[x]) and (self.connect[start][x]!=0):
                    self.visited[x]=True
                    self.dfs(x, target)
        return 0

def main():
    #n: 사건의 개수(400이하 자연수)
    #k: 사건의 전후관계 개수(50000이하 자연수)
    n, k= map(int, sys.stdin.readline().split())

    #역사 객체만들기
    h=History(n)

    #인접리스트 만들기
    for _ in range(k):
        front, rear= map(int, sys.stdin.readline().split())
        h.connect[front-1][rear-1]=-1
        h.connect[rear-1][front-1]=1

    #s입력
    s=int(sys.stdin.readline())
    for _ in range(s):
        start, target=map(int,sys.stdin.readline().split())
        h.visited=[False]*n #방문리스트 초기화
        if h.connect[start-1][target-1]==0:
            print(h.dfs(start-1, target-1))
        else:
            print(h.connect[start-1][target-1])

if __name__=='__main__':
    main() 

```

<hr>

## 시도2
- 코드
