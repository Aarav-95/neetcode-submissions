class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        r = 1
        res = []
        while l < len(temperatures):
            if r >= len(temperatures):
                res.append(0)
                l += 1
                r = l + 1
            elif temperatures[r] > temperatures[l]:
                res.append(r-l)
                l += 1
                r = l + 1
            else:
                r += 1

        return res
            