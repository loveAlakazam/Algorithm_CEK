# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 큐를 만드는 대신에 deque을... ^^;
from collections import deque

class Solution:
    def __init__(self):
        self.q=deque([])
        self.ans=[]
        self.node_level_cnt={} #레벨순회하다가 거친 노드의 레벨
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 루트가 비어있다면 -> 비어있는 self.ans를 리턴..
        if root is None:
            return self.ans
         
        #루트가 가리키는 노드가 존재한다면 큐에 먼저 넣는다.
        #루트노드의 레벨을 0으로 했다.
        self.q.append((root,0)) #(root노드, 레벨)
        
        
        #큐가 비어질때까지 반복
        while len(self.q)>0:
            #가장 먼저 들어온 노드와 그 노드의 레벨을 얻는다.
            node, node_level= self.q.popleft()
             
            if node: #노드가 존재한다면
                # node_level이 self_level_cnt에 있는가?
                if node_level in self.node_level_cnt:
                    self.node_level_cnt[node_level]+=1
                    
                else:
                    self.node_level_cnt[node_level]=1
                    self.ans.append([])
                    
                self.ans[node_level].append(node.val)
                
                #왼쪽 자식노드가 존재한다면
                if node.left is not None:
                    self.q.append((node.left, node_level+1)) #왼쪽 자식노드를 큐에 넣는다.
                #오른쪽 자식노드가 존재한다면
                if node.right is not None:
                    self.q.append((node.right, node_level+1)) #오른쪽 자식노드를 큐에넣는다.
        return self.ans
