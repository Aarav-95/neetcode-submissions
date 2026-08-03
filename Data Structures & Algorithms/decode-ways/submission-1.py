class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = {n: 1}
        def dp(idx):
            if idx in res:
                return res[idx]
            if s[idx] == "0":
                return 0
            result = dp(idx+1)
            if idx + 1 < n and (s[idx] == "1" or (s[idx] == "2" and s[idx+1] in "0123456")):
                result += dp(idx+2)
                res[idx] = result
            return result
        
        return dp(0)