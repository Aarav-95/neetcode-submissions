class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        cur_sum = 0
        length = len(candidates)

        def back(i):
            nonlocal cur_sum
            if cur_sum == target:
                res.append(cur.copy())
                return
            if i >= length or cur_sum > target:
                return
            
            cur.append(candidates[i])
            cur_sum += candidates[i]
            back(i+1)

            cur.pop()
            cur_sum -= candidates[i]

            while i + 1 < length and candidates[i] == candidates[i+1]:
                i+=1
            back(i+1)
        
        back(0)
        return res

