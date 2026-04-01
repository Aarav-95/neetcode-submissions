class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            freq = {}
            for j in i:
                if j in freq:
                    freq[j] += 1
                else:
                    freq[j] = 1
            h = tuple(sorted(freq.items()))
            if h in res:
                res[h].append(i)
            else:
                res[h] = [i]
        ordered = []
        for i in res:
            ordered.append(res[i])
        return ordered