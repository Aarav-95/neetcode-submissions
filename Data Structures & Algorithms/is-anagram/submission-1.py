class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = {}
        t_char = {}

        for i in s:
            if ord(i) in s_char:
                s_char[ord(i)] += 1
            else:
                s_char[ord(i)] = 1
        
        for i in t:
            if ord(i) in t_char:
                t_char[ord(i)] += 1
            else:
                t_char[ord(i)] = 1
        
        for i in s_char:
            if i not in t_char or s_char[i] != t_char[i]:
                return False
        return True


        
        