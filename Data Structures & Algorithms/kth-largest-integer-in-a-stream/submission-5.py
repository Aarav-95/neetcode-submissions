class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.heap = nums.copy()
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        print(self.heap)
        return self.heap[0]
        
