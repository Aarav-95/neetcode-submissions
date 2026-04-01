class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while h >= l:
            mid = (h + l) // 2
            if nums[mid] == target:
                return mid
            elif target >= nums[l] and target <= nums[mid]:
                h = mid - 1
            elif target <= nums[h] and target >= nums[mid]:
                l = mid + 1
            elif nums[mid] > nums[h]:
                l = mid + 1
            elif nums[l] > nums[mid]:
                h = mid - 1
            else:
                return -1
            