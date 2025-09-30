class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        record = Counter() # hashmap char -> int
        left = 0

        for right, c in enumerate(s):
            record[c] += 1
            while record[c] > 1:
                record[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans


            
        