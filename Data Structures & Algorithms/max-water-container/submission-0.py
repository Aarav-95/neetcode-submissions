class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0
        while r > l:
            temp = (r - l) * min(heights[l], heights[r])
            if temp > area:
                area = temp
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return area

