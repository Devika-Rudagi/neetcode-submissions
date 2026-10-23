class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for r,x in enumerate(nums):
            if x in window:
                return True
            window.add(x)
            if len(window)>k:
                window.remove(nums[r-k])
        return False
            
