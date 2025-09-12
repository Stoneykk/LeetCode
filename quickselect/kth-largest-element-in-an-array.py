import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pri_q = []
        for num in nums:
            heapq.heappush(pri_q, num)
            if len(pri_q) > k:
                heapq.heappop(pri_q)
        
        return pri_q[0]
        
