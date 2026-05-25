class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        subset = []
        def back(i):
            if i >= length:
                print(subset)
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            back(i+1)
            subset.pop()
            back(i+1)
            
        
        back(0)
        return res