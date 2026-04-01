class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for i in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, i)
            else:
                if minHeap[0] < i:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, i)

        return minHeap[0]        