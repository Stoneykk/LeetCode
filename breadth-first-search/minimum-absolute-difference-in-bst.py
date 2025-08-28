# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.vec = []
        self.dfs(root, self.vec)

        if len(self.vec) < 2:
            return 0
        result = 2000000
        for i in range(1, len(self.vec)):
            result  = min(result, self.vec[i]-self.vec[i-1])
        return result
    
    
    def dfs(self, root, vec):
        if not root:
            return
        self.dfs(root.left, vec)
        vec.append(root.val)
        self.dfs(root.right, vec)