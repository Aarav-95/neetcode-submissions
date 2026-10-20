class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * (len(nums)+1) for _ in range(len(nums))]

        def back(i, j):
            if i == len(nums):
                return 0
            if dp[i][j+1] != -1:
                return dp[i][j+1]

            LIS = back(i+1, j)

            if j == -1 or nums[i] > nums[j]:
                LIS = max(1 + back(i+1, i), LIS)

            dp[i][j+1] = LIS
            return LIS

        return back(0,-1)
