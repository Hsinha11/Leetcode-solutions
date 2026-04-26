# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        q=[]
        
        q.append(root)
        while q:
            lev=[]
            for i in range(len(q)):
                a=q.pop(0)
                lev.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            res.append(lev)
        for i in range(len(res)):
            res[i]= sum(res[i])/len(res[i])
        return res

        