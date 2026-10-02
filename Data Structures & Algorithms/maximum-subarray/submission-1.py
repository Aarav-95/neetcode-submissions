class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = float('-inf')
        res = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            cur = max(nums[i], nums[i] + cur)
            res = max(res, cur)
        
        return res