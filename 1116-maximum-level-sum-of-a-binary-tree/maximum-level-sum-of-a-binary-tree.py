# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
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
        print(res)
        maxi=-1e9
        idx=-1
        for i in range(len(res)):
            if sum(res[i])>maxi:
                maxi=max(maxi,sum(res[i]))
                idx=i
        return idx+1
        