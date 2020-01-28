# -*- coding: utf-8 -*-
# 참고 소스코드: https://kyunstudio.tistory.com/172
import sys
input=sys.stdin.readline
pre_order_nodes=[]

# 후위순회
def post_order(left, right):
    if left<=right:
        root=pre_order_nodes[left]
        end=right
        while pre_order_nodes[end]>root:
            end-=1
            
        #왼쪽 서브트리
        post_order(left+1, end)
        #오른쪽서브트리
        post_order(end+1,right)
        #현재루트노드
        print(root)
        
def main():
    # 숫자 데이터(전위순회결과)를 입력받는다.
    while True:
        try:
            v=int(input().strip())
            pre_order_nodes.append(v)
        except:
            break
    
    sorted_nodes=sorted(pre_order_nodes)
    reversed_nodes= sorted_nodes[::-1]

    #오름차순 정렬되어있는 상태라면..
    if sorted_nodes==pre_order_nodes:
        for x in reversed_nodes:
            print(x)
    #내림차순 정렬되어있는 상태라면..
    elif reversed_nodes==pre_order_nodes:
        for x in sorted_nodes:
            print(x)
    else:
        length=len(pre_order_nodes)
        left=0
        right=length-1
        post_order(left=left, right=right)    

if __name__=='__main__':
    main()
