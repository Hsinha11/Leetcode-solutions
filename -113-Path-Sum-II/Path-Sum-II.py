def pathSum(root, sum):
    res = []
    def dfs(node, path, s):
        if not node:
            return
        if not node.left and not node.right and node.val == s:
            res.append(path + [node.val])
            return
        dfs(node.left, path + [node.val], s - node.val)
        dfs(node.right, path + [node.val], s - node.val)
    dfs(root, [], sum)
    return res
