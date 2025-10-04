class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        record = defaultdict(int)
        for right, x in enumerate(nums):
            record[x] += 1
            while record[x] > k:
                record[nums[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans