class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        prev, last = nums[-2], nums[-1]

        for i in range(n-3, -1, -1):
            temp = last
            last = max(prev, last)
            prev = temp + nums[i]
        
        return max(prev, last)