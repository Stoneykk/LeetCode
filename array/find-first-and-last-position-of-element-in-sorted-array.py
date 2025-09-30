class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    def binarySearch(self, nums, target, leftBias: bool):
        left = 0
        right = len(nums)-1 # [left, right]
        i = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else: # nums[mid] == target
                i = mid
                if leftBias == True:
                    right = mid - 1
                if leftBias == False:
                    left = mid + 1

        return i