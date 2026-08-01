class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        n = len(s)
        def back(idx):
            if idx == n:
                res.append(curr.copy())
            for i in range(idx, n):
                t = s[idx:i+1]
                if t == t[::-1]:
                    curr.append(t)
                    back(i+1)
                    curr.pop()
        
        back(0)
        return res