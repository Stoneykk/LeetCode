# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[1+idx:len(nums)])

        return root

    """
    root = self.traversal(nums, 0, len(nums)-1)
    return root
    def traversal (self, nums, left, right): #[]
        if left > right:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid-1)
        root.right = self.traversal(nums, mid+1, right)
        return root
    """


        
