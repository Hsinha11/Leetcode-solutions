class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.to_delete_set = set()

    def check(self, root, is_root, result):
        if not root:
            return None
        deleted = root.val in self.to_delete_set
        root.left = self.check(root.left, deleted, result)
        root.right = self.check(root.right, deleted, result)
        if not deleted and is_root:
            result.append(root)
        return None if deleted else root

    def delNodes(self, root, to_delete):
        result = []
        self.to_delete_set = set(to_delete)
        self.check(root, True, result)
        return result
