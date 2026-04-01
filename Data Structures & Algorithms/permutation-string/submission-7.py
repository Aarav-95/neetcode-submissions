class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        res = [0] * 26
        for i in range(len(s1)):
            res[ord(s1[i]) - 97] += 1
        freq = [0] * 26
        l = 0
        r = len(s1) - 1
        length = len(s2)
        for i in range(r + 1):
            freq[ord(s2[i]) - 97] += 1
        while r < length:
            if freq == res:
                return True
            freq[ord(s2[l]) - 97] -= 1
            l += 1
            r += 1
            if r < length:
                freq[ord(s2[r]) - 97] += 1
        return False
