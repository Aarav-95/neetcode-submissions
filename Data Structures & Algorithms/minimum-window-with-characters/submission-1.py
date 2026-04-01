class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f = defaultdict(int)
        for i in t:
            f[i] += 1
        for i in range(len(t) - 1, len(s)):
            for j in range(0, len(s) - i):
                l = j
                r = j+i+1
                subs = s[l:r]
                freq = defaultdict(int)
                for k in subs:
                    freq[k] += 1
                flag = 1
                for k in f:
                    if k not in freq or f[k] > freq[k]:
                        flag = 0
                if flag:
                    return subs
        
        return ""