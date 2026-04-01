class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for j, i in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
            elif i < stack[-1]:
                stack.append(i)
            else: # [30] [0,0,0,0,0,0,0]
                count = 1
                while count <= len(stack) and i > stack[0-count]:
                    if stack[0-count] == -1:
                        count += 1
                        continue
                    res[j-count] = count
                    stack[0-count] = -1
                    count += 1
                stack.append(i)

        return res
            