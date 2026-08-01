class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        curr = []
        def back(idx):
            nonlocal curr
            if idx == n:
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            back(idx+1)
            curr.pop()
            back(idx+1)


        
        back(0)
        return res