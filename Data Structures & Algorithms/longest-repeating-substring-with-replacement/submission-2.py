class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r =0,0
        dicti = defaultdict(int)
        maxLen =0
        for r in range(len(s)):
            dicti[s[r]]+=1
            while (r-l+1) - max(dicti.values()) > k:
                dicti[s[l]]-=1
                l+=1
            maxLen = max(maxLen, r-l+1)
        
        return maxLen


