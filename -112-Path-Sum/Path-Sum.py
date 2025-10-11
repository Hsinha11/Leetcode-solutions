def hasPathSum(root, sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)
