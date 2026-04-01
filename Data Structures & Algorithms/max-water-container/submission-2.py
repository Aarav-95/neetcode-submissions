class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while r > l:
            temp = min(heights[r], heights[l]) * (r - l)
            if temp > area:
                area = temp
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return area