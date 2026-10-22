class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxLen = 0
        uniq = set()
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l+=1
            uniq.add(s[r])
            maxLen = max(maxLen, r-l+1)
        
        return maxLen

            




