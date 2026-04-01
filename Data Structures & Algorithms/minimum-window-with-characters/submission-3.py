class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freqt = {}
        for i in t:
            if i in freqt:
                freqt[i] += 1
            else:
                freqt[i] = 1
        res = s
        flag = 0
        l = 0
        r = 0
        length = len(s)
        while r < length:
            if s[r] in freqt:
                l = r
                temp = freqt.copy()
                while r < length:
                    if s[r] in temp:
                        if temp[s[r]] == 1:
                            del temp[s[r]]
                        else:
                            temp[s[r]] -= 1
                    if len(temp) == 0:
                        if r-l+1 <= len(res):
                            res = s[l:r+1]
                            flag = 1
                        break
                    r += 1
                r = l + 1
            else:
                r += 1
        if flag == 1:
            return res
        return ""