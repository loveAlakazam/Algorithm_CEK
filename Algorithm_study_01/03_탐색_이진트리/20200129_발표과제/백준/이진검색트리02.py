# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline

# 트리노드 객체
class TreeNode:
    def __init__(self, data):
        self.val= data
        self.left=None
        self.right=None

# 이진탐색트리 클래스 생성
class BinarySearchTree:
    def __init__(self):
        #루트노드가 가리키는 노드는 존재하지 않는걸로 초기화
        self.root=None
        self.ans=[]

    # 노드 삽입
    def insert_node(self, key):
        #노드 생성
        new_node= TreeNode(key)
        
        #만일 루트가 가리키는 노드가 존재하지 않는다면
        if self.root is None:
            self.root=new_node
            
        else: #루트노드가 존재한다면
            pre=None  #now의 부모노드
            now= self.root
            while now:
                #키값이 현재 노드값보다 크면-> 오른쪽서브트리로 이동
                pre=now
                if key>now.val:
                    now=now.right
                #키값이 현재 노드값보다 작으면->왼쪽서브트리로 이동
                elif key<now.val:
                    now=now.left
                    
            #now(포인터)가 가리키는 노드가 더이상 없다면..
            #now를 new_node로 한뒤..
            now=new_node
            if key>pre.val:
                pre.right=now
            else:#key<=pre.val
                pre.left=now           
        return self.root
        
    # 후위 순회
    def post_order(self, node):
        #현재노드가 존재한다면
        if node:
            self.post_order(node.left) #왼쪽서브트리 탐색
            self.post_order(node.right) #오른쪽서브트리 탐색
            print(node.val) #현재노드의 값을 출력
            
def main():
    # 숫자 데이터를 입력받는다.
    values=[]
    while True:
        x=input().strip()
        if x=='':
            break
        values.append(int(x))
    
    sorted_values= sorted(values)
    reversed_values= sorted_values[::-1]
    #오름차순 정렬 -> 후위순회결과 내림차순이다.
    if values==sorted_values:
        for v in reversed_values:
            print(v)
    
    #내림차순 정렬 -> 후위순회결과 오름차순이다.
    elif values==reversed_values:
        for v in sorted_values:
            print(v)
    else:
        #이진탐색트리 인스턴스 생성
        bst=BinarySearchTree()
    
        #트리를 생성한다.
        for v in values:
            bst.insert_node(key=v)

        #후위순회
        bst.post_order(bst.root)

if __name__=='__main__':
    main()
