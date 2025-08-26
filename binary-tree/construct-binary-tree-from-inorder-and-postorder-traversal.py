# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)

        seperate_idx = inorder.index(root_val)

        inorder_left = inorder[:seperate_idx]
        inorder_right = inorder[seperate_idx+1:] #左开右闭

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(postorder_left):len(postorder)-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root