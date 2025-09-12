import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        intervals.sort(key = lambda x:x[0])

        heap = []
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start < heap[0]:
                heapq.heappush(heap, cur_end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, cur_end)
        
        return len(heap)