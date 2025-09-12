from collections import defaultdict, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = Counter(nums)
        heap = []
        result = []

        for number, freq in record.items():
            heapq.heappush(heap, (-freq, number))
            
            
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
        

            