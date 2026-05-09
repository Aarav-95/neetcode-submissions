class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = [0] * 26

        for i in tasks:
            l[ord(i)-65] -= 1
        
        t = []
        for j in l:
            if j:
                t.append(j)
        count = 0
        heapq.heapify(t)
        queue = []
        while t or queue:
            if t:
                i = heapq.heappop(t) + 1

                if i < 0:
                    queue.append([i, count + n])

            if queue and count == queue[0][1]:
                add = queue[0]
                queue.pop(0)
                heapq.heappush(t, add[0])
            
            count += 1
        
        return count