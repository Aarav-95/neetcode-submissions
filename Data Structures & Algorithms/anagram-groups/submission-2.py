class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f = {}

        for i in strs:
            freq = [0] * 26;
            for j in i:
                freq[ord(j)-97] += 1
            if tuple(freq) not in f:
                f[tuple(freq)] = []
            f[tuple(freq)].append(i)

        res = []
        for i in f:
            res.append(f[i])
        return res