class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        n = {}

        for i in nums:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1
        
        for i in range(k):
            max = 0
            idx = 0
            for j in n:
                if n[j] > max:
                    max = n[j]
                    idx = j
            freq.append(idx)
            n[idx] = 0

        return freq
            
