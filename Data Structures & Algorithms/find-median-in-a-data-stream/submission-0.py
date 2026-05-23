class MedianFinder:
    def __init__(self):
        self.bottom = [] # maxHeap
        self.top = [] # minHeap
        self.length = 0
    def addNum(self, num: int) -> None:
        if len(self.bottom) == 0:
            heapq.heappush(self.bottom, -num) 
        elif len(self.top) == 0:
            if num < (self.bottom[0] * -1):
                heapq.heappush(self.top, self.bottom[0]*-1)
                heapq.heapreplace(self.bottom, -num)
            else:
                heapq.heappush(self.top, num)
        elif num < self.top[0]:
            if len(self.bottom) > len(self.top):
                node = heapq.heappop(self.bottom)
                heapq.heappush(self.top, node*-1)
                heapq.heappush(self.bottom, -num)
            else:
                heapq.heappush(self.bottom, -num)
        else:
            if len(self.top) > len(self.bottom):
                node = heapq.heappop(self.top)
                heapq.heappush(self.bottom, node*-1)
                heapq.heappush(self.top, num)
            else:
                heapq.heappush(self.top, num)

        self.length += 1

    def findMedian(self) -> float:
        if len(self.bottom) > len(self.top):
            return self.bottom[0] * -1
        elif len(self.top) > len(self.bottom):
            return self.top[0]
        else:
            return ((self.bottom[0]*-1) + (self.top[0])) / 2
   