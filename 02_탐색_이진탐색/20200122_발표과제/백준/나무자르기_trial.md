# 1차시 (26%에서 실패)
```python
# -*- coding: utf-8 -*-
# 이진탐색 : 백준 나무자르기 2805
import sys
input=sys.stdin.readline

def solution():
    N,M =map(int, input().split())
    trees=list( map(int, input().split()) )
    trees.sort()
    max_h=0
    left, right=0, N-1
    while(left<=right):
        mid=(left+right)//2
        h=trees[mid]
        get_rest=sum([tree-h for tree in trees if tree>h])
        if get_rest==M:
            max_h=h
        elif get_rest<M:
            right=mid-1
        else:
            if max_h<h:
                max_h=h
            left=mid+1
    print(max_h)

if __name__=='__main__':
    solution()

```

<br><br>
# 2차시 (10%에서 실패)
```python
# -*- coding: utf-8 -*-
# 이진탐색 : 백준 나무자르기 2805
import sys
input=sys.stdin.readline

def binary_search(N, M, trees):
    left, right =0, N-1
    while(left<=right):
        mid=(left+right)//2
        h=trees[mid]
        
        # N개의 나무를 h만큼 잘라서 상근이가 얻을 수 있는 나무길이
        get_tree= sum( tree-h for tree in trees if tree>h)
        
        print('left: {0}, mid: {1}, right: {2}, h: {3}, get_tree: {4}'.format(left,mid,right,h, get_tree))

        # 절단기에 설정할 수 있는 높이 최댓값이 trees의원소일때
        if get_tree==M:
            return h
        
        # 높이 최댓값이 trees의 오른쪽에 위치할수록 얻을 수 있는 get_tree값이 작음
        # 반면, 왼쪽에 위치할 수록 얻을 수 있는 get_tree값이 큼
        # 얻은나무길이 >상근이 필요 나무길이
        elif get_tree>M:#얻은나무길이>필요한 나무길이 ---> h가 커야함
            left=mid+1

        elif get_tree<M:#얻은나무길이<필요한나무길이 ---> h가 작아야함.
            right=mid-1
    if M>get_tree :
        return 0
    return h
            
def solution():
    # N: 나무개수, M: 상근이가 필요로하는 나무길이(미터)
    N,M =map(int, input().split())
    
    # N개의 나무들 항상 M미터보다 크다.
    trees=list( map(int, input().split()) )
    
    #trees를 오름차순 정렬한다.
    trees.sort()

    # N개의 나무를 H미터만큼 잘랐을때
    # 상근이가 얻을 수 있는 나무길이가 M미터이상일때
    # 절단기에서 설정한 길이(H)중 최대 길이
    H_MAX= binary_search(N,M,trees)
    print(H_MAX)
```

<br><br>
# 3차시 (성공)
- 어떻게하면 여기서 걸리는 시간을 더 줄일 수 있을까?
- sort() -> sorted()를 사용
- sum([for문]) -> sum( for문)
```python
# -*- coding: utf-8 -*-
# 이진탐색 : 백준 나무자르기 2805
import sys
input=sys.stdin.readline
def binary_search(N,M, trees):
    # H=h_left=0 일때 상근이가 얻을 수 있는 나무길이: sum(trees)
    # H= h_right일때 상근이가 얻을수있는 나무길이:  0
    # H 값이 클 수록 상근이가 얻을 수 있는 나무길이값은 작아진다.
    # H 값이 작을수록 상근이가 얻을 수 있는 나무길이값은 커진다.
    h_left=0
    h_right=trees[-1]
    h_values=[]
    while h_left<=h_right:
        h_mid=(h_left+h_right)//2
        get_tree= sum( tree- h_mid for tree in trees if tree>h_mid)
        #print('# h_left: {0}, h_mid:{1}, h_right:{2}\nget_tree:{3}'.format(h_left, h_mid,h_right, get_tree))
        #print('#, h_mid: ',h_mid,'  get_tree: ',get_tree)

        # 상근이가 필요한 나무길이M보다 크게 나온경우는
        # H값을 큰쪽으로 늘리면 얻은 나무길이를 줄일 수 있다.
        if get_tree>=M:
            if get_tree==M:
                return h_mid
            else:
                #h_values.append(h_mid)
                h_left= h_mid+1
        else:# get_tree<M
            #상근이가 필요한 나무길이보다 적게 나온경우는
            #H값을 작은쪽으로 줄여서 얻은나무길이를 늘린다.
            h_right=h_mid-1
    #print('# h_left: {0}, h_mid:{1}, h_right:{2}\nget_tree:{3}'.format(h_left, h_mid,h_right, get_tree))                   
    return h_right

def solution():
    N, M= map(int, input().split())
    trees=list(map(int, input().split()))
    trees=sorted(trees) #나무를 오름차순 정렬
    print(binary_search(N,M,trees))

if __name__=='__main__':
    solution()

```
