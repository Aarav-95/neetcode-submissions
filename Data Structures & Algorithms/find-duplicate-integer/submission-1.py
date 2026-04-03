class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = [0] * 10000

        for i in nums:
            if idx[i] > 0:
                return i
            idx[i] += 1
        