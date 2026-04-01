class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = []

        left = [] # 0, 0, 1, 1, 1, 4
        for i in range(length):
            while stack and heights[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1][1])
            stack.append([heights[i], i])
        
        stack = []
        right = [0] * length

        for i in range(length - 1, -1, -1):
            while stack and heights[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                right[i] = length 
            else:
                right[i] = stack[-1][1]
            stack.append([heights[i], i])
        print(left)
        print(right)
        res = 0
        for i in range(length):
            area = heights[i] * (right[i] - left[i] - 1)
            res = area if area > res else res
        return res