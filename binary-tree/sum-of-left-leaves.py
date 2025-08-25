# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            cur = stack.pop()
            if cur.left and not cur.left.left and not cur.left.right:
                result += cur.left.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result