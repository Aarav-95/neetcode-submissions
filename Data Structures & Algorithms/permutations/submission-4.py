class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        cur = []
    
        def back(remain):
            nonlocal cur
            if len(remain) == 2:
                res.append(cur+remain)
                res.append(cur+remain[::-1])
                if cur:
                    cur.pop()
                return
            for i in range(len(remain)):
                cur.append(remain[i])
                back(remain[:i]+remain[i+1:]) # 1,2
            if cur:
                cur.pop()
        
        back(nums)
        return res
