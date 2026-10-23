class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicti = defaultdict(int)
        l, r =0,0
        #for r in range(k+1):
        while r-l <= k and r<len(nums):
            if nums[r] not in dicti:
                dicti[nums[r]] = r
                r+=1
            else:
                # i = dicti[nums[r]]
                # j = r
                # if abs(i-j) <= k:
                return True
            if r>k:
                del dicti[nums[l]]
                l+=1
        
        return False
            
