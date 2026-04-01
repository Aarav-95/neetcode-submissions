class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = []
        for item in nums:
            if item not in res:
                res.append(item)
        
        maxlen = 0
        temp = 0
        print(res)
        for i in range(0, len(res) - 1):
            if abs(res[i+1] - res[i]) == 1:
                temp += 1
            else:
                if temp > maxlen:
                    maxlen = temp
                temp = 0
        
        return max(temp + 1, maxlen + 1)
        