"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
d = {}
maxi = 1
class Solution:  
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:return 0
        mx = 0
        if root in d:return d[root]
        for i in root.children:
            mx = max(mx,self.maxDepth(i))
        d[root]=1+mx
        return d[root]
