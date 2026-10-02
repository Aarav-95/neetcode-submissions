class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        def greedy(idx):
            if idx == 0:
                return True
            for i in range(1, idx+1):
                if nums[idx-i] >= i:
                    if greedy(idx-i):
                        return True
        
        if greedy(n) == True:
            return True
        
        return False
