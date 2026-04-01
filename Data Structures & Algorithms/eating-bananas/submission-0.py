class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l = 0
        temp = m
        while m >= l:
            mid = (m + l) // 2
            if mid == 0:
                break
            t = 0
            for i in piles:
                t += math.ceil(i / mid)
            if t > h:
                l = mid + 1
            elif t <= h:
                if mid < temp:
                    temp = mid
                m = mid - 1
        return temp