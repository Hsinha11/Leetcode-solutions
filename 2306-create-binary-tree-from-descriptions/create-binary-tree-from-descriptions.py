# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descr: List[List[int]]) -> Optional[TreeNode]:
        d= {}
        hasparent = {}
        for i,j,k in descr:
            hasparent[j]=True
            if i not in d:
                n = TreeNode(i)
                d[i]= n
            if j not in d:
                n = TreeNode(j)
                d[j] = n
        for i in d:
            if i not in hasparent:
                root = i
                break
        for i,j,k in descr:
            if k==1:
                d[i].left=d[j]
            else:
                d[i].right=d[j]
        return (d[root])
        
                

