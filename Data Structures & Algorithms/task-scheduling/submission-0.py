class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f = {}
        for i in tasks:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        maxHeap = []
        for i in f:
            maxHeap.append(f[i] * -1)

        heapq.heapify(maxHeap)
        q = []
        count = 0

        while maxHeap or q:
            if maxHeap:
                i = heapq.heappop(maxHeap) + 1
                if i < 0:
                    q.append([i, count + n])

            if q and count == q[0][1]:
                add = q[0]
                q.pop(0)
                heapq.heappush(maxHeap, add[0])

            count += 1

        return count
