class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = {}
        for n in strs:
            arr = [0] * 26
            for j in n:
                arr[ord(j) - 97] += 1
            if tuple(arr) not in strmap:
                strmap[tuple(arr)] = [n]
            else:
                strmap[tuple(arr)].append(n)
        return list(strmap[i] for i in strmap)
        
            
