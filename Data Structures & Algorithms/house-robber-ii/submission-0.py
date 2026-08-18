class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def houseRob(houses):
            p2, p1 = 0,0
            for i in houses:
                p2, p1 = p1, max(p1, p2+i)
            return p1
        return max(houseRob(nums[:-1]), houseRob(nums[1:]))
        #excluding last house, excluding first house
        
