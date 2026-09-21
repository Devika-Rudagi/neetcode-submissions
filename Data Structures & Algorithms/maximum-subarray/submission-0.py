class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, total =0,-1
        for num in nums:
            if cur <0:
                cur =0
            cur+=num
            total = max(cur, total)
        
        return total