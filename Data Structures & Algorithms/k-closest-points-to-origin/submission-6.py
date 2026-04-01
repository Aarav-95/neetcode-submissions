class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        res = []

        for i in points:
            distance = math.sqrt((i[0])**2 + (i[1])**2)
            
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, distance*-1)
                
            
            else:
                dmax = abs(maxHeap[0])
                if distance < dmax:
                    heapq.heappop(maxHeap)
                    
                    heapq.heappush(maxHeap, distance*-1)
            
            
            print(maxHeap)
        
        for i in points:
            distance = math.sqrt((i[0])**2 + (i[1])**2)
            
            if distance <= abs(maxHeap[0]) and len(res) < k:
                res.append(i)
         
        return res
        



