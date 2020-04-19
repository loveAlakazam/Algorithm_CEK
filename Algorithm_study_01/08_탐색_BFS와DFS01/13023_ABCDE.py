# -*- coding: utf-8 -*-
#인접리스트를 활용한 DFS 그래프 탐색
import sys
global visited
global f
global N

def dfs(i, cnt): #i: 노드번호, cnt: 친구관계수
    #노드 i를 방문을 한다
    visited[i]=True
    #print('\n현재 i: ', i)
    #print('cnt: ', cnt)
    #print('visited: ', visited)
    
    #모든 노드가 다 방문했다면
    if cnt==4:
        return True
    
    for j in f[i]: #노드 i와 연결된 노드들의 집합 f[i]
        #방문하지 않은 노드를 먼저 탐색
        if visited[j] is False:
            #cnt+1: i와 j를 연결을 한다.(간선 추가)
            if(dfs(j, cnt+1)):#만일 cnt==4인경우가 나온다면
                return 1

    #백트래킹했을 때 모든 노드들이 방문되는걸 막기위해서
    visited[i]=False
    return 0

def main():
    answer=0
    for i in range(N):
        if dfs(i,0):
            answer=1
            break
    print(answer)

if __name__=='__main__':
    #N과 M을 입력
    N,M=map(int, sys.stdin.readline().split())

    #visited:노드 방문 리스트
    visited=N*[False]

    #인접리스트를 만듭니다.
    f= [ []*N for _ in range(N)]
    
    #그래프 관계를 맺습니다.
    for m in range(M):
        i,j= map(int, sys.stdin.readline().split())
        f[i].append(j) #i와 j연결
        f[j].append(i) #j와 i연결
        
    result=main()
