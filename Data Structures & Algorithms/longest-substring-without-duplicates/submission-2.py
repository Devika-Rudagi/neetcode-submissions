class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxLen = 0
        map = {}
        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]] +1, l)
            map[s[r]] = r
            maxLen = max(maxLen, r-l+1)
        
        return maxLen

            




