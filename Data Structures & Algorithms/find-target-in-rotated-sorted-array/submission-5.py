class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while r >= l:
            mid = l + ((r-l) // 2)

            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            if nums[mid] >= nums[l]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            print(l,r)
        return -1