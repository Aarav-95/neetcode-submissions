class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        res = s[0]
        res_len = 1
        for i in range(0, n-1):
            curr_len = 1
            o = 1
            while i-o > -1 and i+o < n and s[i-o] == s[i+o]:
                curr_len += 2
                o += 1
            
            if curr_len > res_len:
                res = s[i-o+1:i+o]
                res_len = curr_len
            
            if s[i] == s[i+1]:
                curr_len = 2
                o = 1
                while i-o > -1 and i+1+o < n and s[i-o] == s[i+1+o]:
                    curr_len += 2
                    o += 1
            
                if curr_len > res_len:
                    res = s[i-o+1:i+o+1]
                    res_len = curr_len
            
        return res