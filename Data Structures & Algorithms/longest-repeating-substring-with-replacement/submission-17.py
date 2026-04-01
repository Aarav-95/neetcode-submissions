class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxf = 0
        letter = ''
        l = 0
        r = 0
        res = 0
        length = len(s)
        while r < length:
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            maxf = max(maxf, freq[s[r]])
            while r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res