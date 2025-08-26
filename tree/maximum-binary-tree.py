# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        root = TreeNode(0)
        maxnum = 0
        max_idx = 0
        for i in range(len(nums)):
            if nums[i] > maxnum:
                maxnum = nums[i]
                max_idx = i
        root.val = maxnum

        if max_idx > 0: #左边还有
            left_list = nums[:max_idx]
            root.left = self.constructMaximumBinaryTree(left_list)
        if max_idx < len(nums)-1: #右边还有
            right_list = nums[1+max_idx:len(nums)]
            root.right = self.constructMaximumBinaryTree(right_list)

        return root
        