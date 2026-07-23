class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        run = 1
        for i in range(1, len(nums)):
            run *= nums[i-1]
            prefix.append(run)
        rev = nums[::-1]
        run = 1
        for i in range(1, len(rev)):
            run *= rev[i-1]
            suffix.append(run)
        suffix = suffix[::-1]
        res = []
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res