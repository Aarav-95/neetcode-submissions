class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        visited = set()

        def back(i):
            if s[i:] in visited:
                return False
            if i == len(s):
                return True
            
            for j in range(i, len(s)+1):
                if s[i:j] in words:
                    if back(j):
                        return True

            visited.add(s[i:])
        
        if back(0):
            return True

        return False
                