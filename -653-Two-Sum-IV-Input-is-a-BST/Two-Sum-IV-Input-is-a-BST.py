def findTarget(root, k):
    s = set()
    def dfs(node):
        if not node: return False
        if k - node.val in s: return True
        s.add(node.val)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)
