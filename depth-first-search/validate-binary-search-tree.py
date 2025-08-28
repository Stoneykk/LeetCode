# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        inorder = []
        self.dfs(root, inorder)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
        return True
    def dfs(self, root, inorder):
        if not root:
            return
        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)