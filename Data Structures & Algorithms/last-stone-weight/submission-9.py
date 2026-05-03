class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        
        while len(stones) > 1:
            sec = stones[1]
            if len(stones) > 2:
                sec = stones[1] if stones[1] < stones[2] else stones[2] 
            if stones[0] == sec:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                diff = (stones[0]*-1) - (sec*-1)
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, (diff*-1))
        
        return (stones[0]*-1) if stones else 0
