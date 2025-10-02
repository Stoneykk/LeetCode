class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        ans = 0
        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                ans += right - left
                left += 1
        return ans



