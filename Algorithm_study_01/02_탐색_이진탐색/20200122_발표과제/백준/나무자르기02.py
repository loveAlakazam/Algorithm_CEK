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
    while h_left<=h_right:
        h_mid=(h_left+h_right)//2
        get_tree= sum( tree- h_mid for tree in trees if tree>h_mid)

        # 상근이가 필요한 나무길이M보다 크게 나온경우는
        # H값을 큰쪽으로 늘리면 얻은 나무길이를 줄일 수 있다.
        if get_tree>=M:
            if get_tree==M:
                return h_mid
            else:
                h_left= h_mid+1
        else:# get_tree<M
            #상근이가 필요한 나무길이보다 적게 나온경우는
            #H값을 작은쪽으로 줄여서 얻은나무길이를 늘린다.
            h_right=h_mid-1
    return h_right

def solution():
    N, M= map(int, input().split())
    trees=list(map(int, input().split()))
    trees=sorted(trees) #나무를 오름차순 정렬
    print(binary_search(N,M,trees))

if __name__=='__main__':
    solution()
