# 이진검색트리
## 시도1
- 결과: 18%에서 Runtime Error
- 코드
```python

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

    # 노드 삽입
    def insert_node(self, key):
        #노드 생성
        new_node= TreeNode(data=key)
        
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
            else: # key<=pre.val
                pre.left=now
                
                    
    # 전위순회
    def pre_order(self, node):
        #현재노드가 존재한다면
        if node:
            print(node.val) #현재 노드값 출력
            self.pre_order(node=node.left)#왼쪽서브트리 탐색
            self.pre_order(node=node.right)#오른쪽서브트리 탐색
        

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
    #print(values)
        
    #이진탐색트리 인스턴스 생성
    bst=BinarySearchTree()
    
    #트리를 생성한다.
    for v in values:
        bst.insert_node(key=v)

    #전위순회로 먼저 확인
    bst.pre_order(bst.root)

    #후위순회
    bst.post_order(bst.root)

if __name__=='__main__':
    main()

```
- 틀린이유: 1,2,3,4,5,... 와 같이 연속된 수인 경우에는 일자선으로 불균형한 트리
- 만일 1,2,3, ..., 9999 즉 1만개의 노드가 있다면<br>
  RecursionError maximum recursion depth exceeded라는 에러가 뜬다.
- 참고: https://www.acmicpc.net/board/view/26171

# 시도2
