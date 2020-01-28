# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=[]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #왼쪽서브트리 -> 루트노드데이터 -> 오른쪽서브트리
        if root: #루트노드가 존재한다면
            self.inorderTraversal(root.left) #왼쪽서브트리 탐색
            self.ans.append(root.val) #데이터 삽입
            self.inorderTraversal(root.right) #오른쪽서브트리 탐색
            
        # 더이상 루트가 존재하지 않는다면.. 
        return self.ans
