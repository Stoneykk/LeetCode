class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
        
    def backtracking(self, s, start_idx, path, result):
        if start_idx == len(s):
            result.append(path[:])
            return
        for i in range(start_idx, len(s)):
            if self.is_palindrome(s, start_idx, i):
                path.append(s[start_idx:i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

    def is_palindrome(self, s, start, end)->bool:
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        return True