class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        ans = 1
        same = 0
        for right in range(1, len(s)):
            if s[right] == s[right-1]:
                same += 1
            if same > 1:
                left += 1
                while s[left] != s[left-1]:
                    left += 1
                same = 1
            ans = max(ans, right-left+1)
        
        return ans


            
