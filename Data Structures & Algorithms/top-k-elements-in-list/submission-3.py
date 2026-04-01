class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        res = []

        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        
        for i in range(k):
            maxNum = nums[0]
            for j in f:
                if f[j] > f[maxNum]:
                    maxNum = j
            res.append(maxNum)
            f[maxNum] = 0
        
        return res
