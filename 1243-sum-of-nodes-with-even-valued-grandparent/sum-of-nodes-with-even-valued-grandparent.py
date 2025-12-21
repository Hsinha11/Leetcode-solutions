# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        parent = {}
        parent[root]=None
        def dfs(root):
            if root==None:
                return
            if root.left:
                parent[root.left]=root
                dfs(root.left)
            if root.right:
                parent[root.right]=root
                dfs(root.right)
        dfs(root)
        c = 0
        for i in parent:
            if parent.get(parent.get(i,None),None)!=None and parent[parent[i]].val%2==0:
                c+=i.val
        return c
