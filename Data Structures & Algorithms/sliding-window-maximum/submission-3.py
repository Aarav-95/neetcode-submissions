class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [[nums[i], i] for i in range(0, k)]
        heapq._heapify_max(maxHeap)
        res = [maxHeap[0][0]]
        l = 0
        for i in range(k, len(nums)):
            heapq.heappush_max(maxHeap, [nums[i], i])
            while maxHeap and maxHeap[0][1] <= l:
                heapq.heappop_max(maxHeap)

            res.append(maxHeap[0][0])
            l += 1
        return res