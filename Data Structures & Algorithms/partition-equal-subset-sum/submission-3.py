class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        
        dp = [[-1] * (target+1) for _ in range(len(nums)+1)]

        def back(i, total):
            if i >= len(nums):
                return False

            total += nums[i]
            if target == total:
                return True
            if total > target:
                return False
            if dp[i][total] != -1:
                return dp[i][total]
            
            dp[i][total] = back(i+1, total) or back(i+1, total-nums[i])
            return dp[i][total]
        if back(0, 0):
            return True
        
        return False