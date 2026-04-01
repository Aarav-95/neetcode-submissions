class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = []
        count = 0
        for i in nums:
            count += 1
        
        for i in range(count):
            prod = 1
            for j in range(count):
                if j != i:
                    prod *= nums[j]
            p.append(prod)
        return p

