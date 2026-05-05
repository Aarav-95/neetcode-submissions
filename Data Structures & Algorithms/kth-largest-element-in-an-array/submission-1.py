class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, i)
            else:
                if i > minHeap[0]:
                    heapq.heapreplace(minHeap, i)
        
        return minHeap[0]