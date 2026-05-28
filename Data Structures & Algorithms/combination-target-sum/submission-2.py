class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        curr_sum = 0 
        length = len(nums)
        def back(i):
            nonlocal curr_sum, length
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr.copy())
                return
            if i >= length:
                return

            curr.append(nums[i])
            curr_sum += nums[i]
            back(i)

            curr.pop()
            curr_sum -= nums[i]
            back(i+1)
        
        back(0)
        return res