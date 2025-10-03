class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        diff = float('inf')
        for i in range(n):
            if nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s > target:
                    if s - target < diff:
                        diff = s - target
                        ans = s
                    k -= 1
                else: # s < target
                    if target - s < diff:
                        diff = target - s
                        ans = s
                    j += 1
        return ans