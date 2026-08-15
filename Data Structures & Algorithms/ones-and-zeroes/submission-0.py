class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(m, n, i):
            if i == len(strs):
                return 0
            if (m, n, i) in dp:
                return dp[(m,n,i)]
            
            mCnt = strs[i].count('0')
            nCnt = strs[i].count('1')

            dp[(m, n, i)] = dfs(m,n,i+1)
            if mCnt <= m and nCnt <= n:
                dp[(m, n, i)] = max(dp[(m, n, i)], 1 + dfs(m-mCnt, n-nCnt, i+1))        

            return dp[(m, n, i)]
    
        return dfs(m,n, 0)