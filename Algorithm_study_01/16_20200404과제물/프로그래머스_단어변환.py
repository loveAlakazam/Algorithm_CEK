import sys
from copy import copy
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
min_cnt=51

def count_diff(now, word):
    cnt=0
    for n, w in zip(now, word):
        if n!=w:
            cnt+=1
    return cnt

def dfs(now, target, words, cnt, visited):
    global min_cnt

    #now가 target과 같은가?
    if now==target:
        min_cnt=min(min_cnt, cnt)
        
    #now와의 차이가 1개인가?
    for word in words:
        if (count_diff(now, word)==1) and (visited[word]==0):
            tmp=copy(visited) #방문리스트를 복사한다.
            tmp[word]=1
            dfs(word, target, words, cnt+1, tmp)

def solution(begin, target, words):
    global min_cnt
    # target이 words에 없는가? -> 0 리턴
    if target not in words:
        return 0

    #방문리스트 초기화
    visited=dict()
    for word in words:
        visited[word]=0
        
    # target이 words에 있다면..
    dfs(begin, target, words, 0, visited)
    return min_cnt
    
def main():
    begin=input().strip()
    target=input().strip()
    words=input().strip().split(',')
    return solution(begin, target, words)

if __name__=='__main__':
    print(main())
