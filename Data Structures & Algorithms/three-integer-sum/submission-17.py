class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                sol.append([nums[0], nums[1], nums[2]])
                return sol
        nums.sort()
        f = {}
        for i in range(0, len(nums)-1):
            if nums[i] in f:
                continue
            else:
                f[nums[i]] = 1
            left = i+1
            right = len(nums)-1
            while right > left:
                target = -1 * nums[i]
                val = nums[left] + nums[right]
                if target == val:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif target > val:
                    left += 1
                else:
                    right -= 1
        l = {}
        for i in range(len(sol)-1, -1, -1):
            if tuple(sol[i]) in l:
                sol.remove(sol[i])
            else:
                l[tuple(sol[i])] = 1
        return sol


                
                