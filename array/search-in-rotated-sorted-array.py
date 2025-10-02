class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 画图，最左最右确定target在哪半条线
        # [left] <= [mid]: 左半边线
        # [left] > [mid]: 右半边线
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] > nums[left]: #左半
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else: #右半 nums[mid] < nums[left]
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


