class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        maxHeap = stones
        
        while len(maxHeap) >= 2:
            great = maxHeap[1]
            if len(maxHeap) > 2:
                if maxHeap[2] < maxHeap[1]:
                    great = maxHeap[2]
                else:
                    great = maxHeap[1]

            if maxHeap[0] == great:
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
            
            else:
                temp = maxHeap[0] - great
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, temp)
            print(maxHeap)

        return abs(maxHeap[0]) if len(maxHeap) > 0 else 0