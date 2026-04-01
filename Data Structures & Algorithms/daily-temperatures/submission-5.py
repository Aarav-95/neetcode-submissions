class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        l = 0
        r = 1
        length = len(temperatures)
        while r < length:
            if temperatures[r] > temperatures[l]:
                res.append(r-l)
                while stack and temperatures[r] > stack[-1][0]:
                    res[stack[-1][1]] = r - stack[-1][1]
                    stack.pop()
            else:
                res.append(0)
                stack.append([temperatures[l], l])
            r += 1
            l += 1
        res.append(0)
        return res