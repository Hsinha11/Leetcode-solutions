def maxPathSum(root):
    res = [float('-inf')]
    def dfs(node):
        if not node: return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        res[0] = max(res[0], node.val + left + right)
        return node.val + max(left, right)
    dfs(root)
    return res[0]
