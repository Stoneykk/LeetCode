class Solution:
    def canJump(self, nums: List[int]) -> bool:
        area = 0
        if len(nums) == 1:
            return True
        i = 0
        while i <= area:
            area = max(i+nums[i], area)
            if area >= len(nums) -1:
                return True
            i += 1
        return False

        