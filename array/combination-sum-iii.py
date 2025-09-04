class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 0, 1, result, [])
        return result
    def backtracking(self, targetSum, k, currentSum, start_idx, result, path):
        if currentSum > targetSum:
            return
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(start_idx, 11-(k-len(path))):
            currentSum += i
            path.append(i)
            self.backtracking(targetSum, k, currentSum, i+1, result, path)
            currentSum -= i
            path.pop()