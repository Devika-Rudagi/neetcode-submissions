class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Two pointers
        rI, rL = 0, 0
        n = len(s)

        def expand(l, r):
            nonlocal rI, rL
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > rL:
                    rI = l
                    rL = r-l+1
                
                l-=1
                r+=1
        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        
        return s[rI: rI+rL]


        