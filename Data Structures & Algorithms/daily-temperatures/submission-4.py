class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(0, len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
            if len(res) < i+1:
                res.append(0)
        
        
        return res