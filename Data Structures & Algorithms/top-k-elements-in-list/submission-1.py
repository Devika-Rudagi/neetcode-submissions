class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        heap = []
        res = []
        for num in counter:
            heapq.heappush(heap, (counter[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        while heap:
            freq, num = heapq.heappop(heap)
            res.append(num)
        
        return res
