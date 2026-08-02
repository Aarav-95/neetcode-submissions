class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            prev, last = nums[-2], nums[-1]

            for i in range(n-3, -1, -1):
                temp = last
                last = max(last, prev)
                prev = nums[i] + temp

            return max(prev, last)

        if n == 1:
            return nums[0]
        return max(dfs(nums[1:]), dfs(nums[:n-1]))
        