# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=[]
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 루트노드 데이터 -> 왼쪽서브트리 -> 오른쪽 서브트리
        if root: #만일 루트노드가 존재한다면
            self.ans.append(root.val) #루트노드
            self.preorderTraversal(root.left)#왼쪽서브트리
            self.preorderTraversal(root.right)#오른쪽서브트리
            
        return self.ans
