class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_nums = []

        for i in nums:
            if i in prev_nums:
                return True
            prev_nums.append(i)
        return False
