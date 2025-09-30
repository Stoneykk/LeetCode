class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf') #初始化无穷大
        cur_sum = 0
        left = 0

        for right, x in enumerate(nums): # x -> nums[right]
            cur_sum += x
            while cur_sum >= target:
                result = min(result, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        
        return result if result <= n else 0
