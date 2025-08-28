# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            node = TreeNode(val)
            return node

        cur = root
        parent = root
        while cur:
            parent = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root   
        
