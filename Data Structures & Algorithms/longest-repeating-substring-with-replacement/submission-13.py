class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        for i in range(len(s), 0, -1):
            for j in range(0, len(s) - i + 1):
                subs = s[j:j+i]
                f = {}
                for l in subs:
                    if l in f:
                        f[l] += 1
                    else:
                        f[l] = 1
                maxlen = max(f.values())
                if maxlen + k >= i:
                    return i
        return i