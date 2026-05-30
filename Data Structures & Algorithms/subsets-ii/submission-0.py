class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        length = len(nums)
        def back(i):
            if i >= length:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            back(i+1)

            subset.pop()
            while i < length-1 and nums[i] == nums[i+1]:
                i += 1
            back(i+1)
        
        back(0)
        return res