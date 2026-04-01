class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while h >= l:
            mid = (h + l) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[l] > nums[mid]:
                h = mid - 1
            elif nums[h] < nums[mid]:
                l = mid + 1
            else:
                return nums[l]
