# -*- coding: utf-8 -*-
# 플로이드 와샬..
import sys
class History:
    def __init__(self, n):
        self.n= n
        self.connect=[ [0]*n for _ in range(n)] #인접리스트
        self.visited=None #방문리스트

    def floyd(self):
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if (x==y) or (y==z) or (x==z):
                        continue
                    else:
                        if self.connect[y][z]==0:
                            #y가 x보다 뒤에 일어난 사건이고(x->y)
                            #x가 z보다 뒤에 일어난 사건이라면(z->x)
                            #y가 z보다 뒤에 일어난 사건이다.(z->x->y )==> (z->y)
                            if (self.connect[y][x]==1) and (self.connect[x][z]==1):
                                self.connect[y][z]=1

                            #y가 x보다 앞에 일어난 사건(y->x)
                            #x가 z보다 앞에 일어난 사건(x->z)
                            #y가 z보다 앞에 일어난 사건이다 (y->x->z)==>(y->z)
                            elif (self.connect[y][x]==-1) and (self.connect[x][z]==-1):
                                self.connect[y][z]=-1
                            
                            

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

    h.floyd() #floyd 와샬
    
    #s입력
    s=int(sys.stdin.readline())
    for _ in range(s):
        start, target=map(int,sys.stdin.readline().split())
        h.visited=[False]*n #방문리스트 초기화
        print(h.connect[start-1][target-1])

if __name__=='__main__':
    main() 
