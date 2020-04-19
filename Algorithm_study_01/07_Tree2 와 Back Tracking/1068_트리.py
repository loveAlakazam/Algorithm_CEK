# -*- coding: utf-8 -*-
import sys
class TreeNode:
    def __init__(self, node_num, val):
        self.node_num=node_num #노드번호
        self.val=val #노드값
        self.left=None #왼쪽자식 링크
        self.right=None #오른쪽자식 링크
        
class Tree:
    def __init__(self):
        self.root=None
        self.cnt_leaf=0 #리프노드의 개수
        
        #루트노드의 부모는 없으므로 -1로 초기화
        self.tree_node_num=-1 

    def insert_node(self, node_num, target_val):
        #노드를 생성한다.
        new_node= TreeNode(node_num=node_num, val=val)
        
        #루트노드가 존재하지 않으면
        if self.root is None:
            self.root=new_node
            
        #루트노드가 존재한다면
        else:
            now=self.root
            while now:
                now
            #node_num이 홀수라면->now의 왼쪽자식
            if node_num%2!=0:
            #node_num이 짝수라면-> now의 오른쪽자식
            else:
            
            
    def delete_target_node(self, target_num):
        #target_num을 찾아서 탐색한다.
        #삭제노드가 리프노드 => 그냥지우면 끝
        #삭제노드가 자식이 한개인 노드=> 자식이 삭제노드의 위치로 올라오면됨.
        #삭제노드가 자식이 두개인 노드=> 왼쪽자식중 가장큰값, 오른쪽자식중 가장 작은값중 하나가 올라온다.
        print()
        
    def count_leaf_node(self, node):
        # 노드가 존재한다면
        if node:
            #전위순회
            print(node.node_num, node.val, self.cnt_leaf)
            if (node.left is None) and (node.right is None):
                self.cnt_leaf+=1
                
            #왼쪽서브트리
            self.count_leaf_node(node.left)
            #오른쪽서브트리
            self.count_leaf_node(node.right)
        return self.cnt_leaf

def main():
    N=int(sys.stdin.readline())
    nodes=list(map(int, sys.stdin.readline().split()))
    target_num=int(sys.stdin.readline())#지울노드번호
    #01. nodes 리스트에 있는 노드들을 생성하여 트리를 만든다.
    t=Tree() #트리객체 생성
    for node_num, val in enumerate(nodes):
        t.insert_node(node_num, val)
    
    #02. node_num이 target_num에 해당하는 노드를 찾는다.
    #target_num 노드를 지운뒤 리프노드의개수를 찾는다.
    result=t.count_leaf_node(t.root)
    print(result)


if __name__=='__main__':
    main()
