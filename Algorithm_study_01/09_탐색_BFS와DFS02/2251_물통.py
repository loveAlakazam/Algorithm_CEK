# -*- coding: utf-8 -*-
import sys
from collections import deque
class Buckets:
    def __init__(self, A,B,C):
        self.A=A
        self.B=B
        self.C=C
        
        #visited[a-1][b-1][c-1] 방문여부
        self.visited=[ [[False]*(A+1) for _ in range(B+1)] for _ in range(C+1)]
        self.result=[]
        self.q=deque()

    def bfs(self):
        self.q.append((0,0,self.C)) #(0,0,C)
        
        while self.q:
            a,b,c= self.q.popleft()

            #방문했는지 확인
            if not self.visited[c][b][a]:
                self.visited[c][b][a]=True

                #A에 들어있는  물의양이 0일때
                if a==0:
                    self.result.append(c)

                #a->b :a를 b에 넣는다
                if (a+b>self.B):
                    self.q.append((a+b-self.B, self.B, c))
                else:
                    self.q.append((0, a+b, c))
                    
                #a->c:  a를 c에 넣는다.
                if(a+c>self.C):
                    self.q.append((a+c-self.C, b, self.C))
                else:
                    self.q.append((0,b, a+c))
                    
                #b->a: b를 a에 넣는다
                if(a+b>self.A):
                    self.q.append((self.A, a+b-self.A, c))
                else:
                    self.q.append((a+b,0,c))
                    
                #b->c: b를 c에 넣는다
                if(b+c>self.C):
                    self.q.append((a, b+c-self.C, self.C))
                else:
                    self.q.append((a,0,b+c))
                    
                #c->a: c를 a에 넣는다
                if(c+a>self.A):
                    self.q.append((self.A, b, c+a-self.A))
                else:
                    self.q.append((a+c,b,0))
                    
                #c->b: c를 b에 넣는다.
                if(c+b>self.B):
                    self.q.append((a, self.B, c+b-self.B))
                else:
                    self.q.append((a, c+b,0))

def main():
    A,B,C= map(int, sys.stdin.readline().split())
    bucket=Buckets(A,B,C)
    bucket.bfs()
    bucket.result=sorted(bucket.result)
    print(' '.join(map(str,bucket.result)))
    
if __name__=='__main__':
    main()


