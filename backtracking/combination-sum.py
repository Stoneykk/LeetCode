class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

    def backtracking(self, candidates, target, current_sum, start_idx, path, result):
        if current_sum > target:
            return
        if current_sum == target:
            result.append(path[:])
            return
        for i in range(start_idx, len(candidates)):
            current_sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, current_sum, i, path, result)
            current_sum -= candidates[i]
            path.pop()
        
