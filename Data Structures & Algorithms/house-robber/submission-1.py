class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = [nums[0], nums[1]]

        for i in range(2, len(nums)):
            res.append(nums[i] + res[0])
            if res[0] < res[1]:
                res.pop(0)
            else:
                res.pop(1)
        
        return max(res[0], res[1])
                