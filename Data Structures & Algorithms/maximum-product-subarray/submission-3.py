class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minp = nums[0]
        maxp = nums[0]
        res = 0
        for num in nums[1:]:
            temp = minp
            minp = min(maxp * num, minp * num, num)
            maxp = max(maxp * num, temp * num, num)
            res = max(maxp, res)
        return res