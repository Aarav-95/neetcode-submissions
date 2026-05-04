class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for i in points:
            dist = math.sqrt(i[0]**2 + i[1]**2)

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, [-dist, i])
            else:
                if abs(maxHeap[0][0]) > dist:
                    heapq.heapreplace(maxHeap, [-dist, i])
        
        res = []
        for i in maxHeap:
            res.append(i[1])
        
        return res