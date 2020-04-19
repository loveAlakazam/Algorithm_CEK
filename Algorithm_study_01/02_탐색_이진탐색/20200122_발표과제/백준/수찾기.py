# -*- coding: utf-8 -*-
# 이진탐색: 백준- 수찾기 1920
import sys
input=sys.stdin.readline

def solution():
    N= int(input())
    A= list( map(int, input().split() ))
    M= int(input())
    L= list( map(int, input().split()))
    #A를 오름차순으로 정렬한다.
    A.sort()
    
    #리스트 L의 원소 M개가 리스트 A에 존재하는가?
    for l in L:
        # 맨왼쪽: 0번째 인덱스
        # 맨오른쪽: N-1번째 인덱스
        left, right= 0,N-1

        # 맨왼쪽(맨오른쪽) 원소가 리스트 L의 원소인경우
        if l==A[left] or l==A[right]:
            print(1)
            
        else:
            while(left<=right):
                mid=(left+right)//2
                if A[mid]==l:
                    print(1)
                    break
                
                elif l>A[mid]: # l이 A[mid]보다 오른쪽에 있는 경우
                    left=mid+1
                    
                elif l<A[mid]: # l이 A[mid]보다 왼쪽에 있는 경우
                    right=mid-1
                    
            # left>right가 되기 직전
            # 마지막 left<=right조건을 만족할때의 mid일때
            # A[mid]가 l과 일치하지 않는다면 0을 출력.
            if A[mid]!=l:
                print(0)
                    
if __name__=='__main__':
    solution()
