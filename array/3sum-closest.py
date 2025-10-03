class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        diff = float('inf')
        for i in range(n-2):
            # 1. 遇到相同的跳过
            if nums[i] == nums[i-1]:
                continue
            # 2. 有序+前3个已经大于target,后面的只会越来越远
            s = nums[i] + nums[i+1] + nums[i+2]
            if i and s > target:
                if s - target < diff:
                    ans = s
                    break
            # 3. 有序+与最后两数之和还是小于target，前面的只会越差越多
            s = nums[i] + nums[-1] + nums[-2]
            if s < target:
                if target - s < diff:
                    diff = target - s
                    ans = s
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