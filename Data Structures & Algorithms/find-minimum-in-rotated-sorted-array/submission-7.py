class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = 1001
        while r > l:
            mid = l + ((r-l) // 2)
            res = nums[mid] if nums[mid] < res else res
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        
        if r == l and nums[r] < res:
            res = nums[r]
        return res