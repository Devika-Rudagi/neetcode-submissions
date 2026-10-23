class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r =0,0
        dicti = defaultdict(int)
        maxLen =0
        maxf = 0
        for r in range(len(s)):
            dicti[s[r]]+=1
            maxf = max(maxf, dicti[s[r]])
            while (r-l+1) - maxf > k:
                dicti[s[l]]-=1
                l+=1
            maxLen = max(maxLen, r-l+1)
        
        return maxLen


