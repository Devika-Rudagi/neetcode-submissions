class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contSet = set(nums)
        long = 0
        for num in contSet:
            if (num-1) not in contSet:
                seqlen = 1
                while (num+seqlen) in contSet:
                    seqlen+=1
                long = max(long, seqlen)
        return long
         