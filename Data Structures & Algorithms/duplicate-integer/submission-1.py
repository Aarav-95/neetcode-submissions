class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_nums = {}

        for i, n in enumerate(nums):
            if n in prev_nums:
                return True
            prev_nums[n] = i
        return False
