class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles) - 1
        k_temp = max(piles)
        while r >= l:
            mid = l + ((r-l) // 2)
            if mid <= 0:
                break
            temp = 0
            for i in piles:
                if i % mid == 0:
                    temp += (i // mid)
                else:
                    temp += (i // mid) + 1
            print(mid, temp)
            if temp > h:
                l = mid + 1
            else:
                k_temp = mid if mid < k_temp else k_temp
                r = mid - 1
            print(l, r)
        return k_temp