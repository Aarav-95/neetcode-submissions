class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        new = ""
        temp = ""
        while (r < len(s)):
            if temp == "":
                char = {}
                temp += s[l]
                char[s[l]] = 1
            if s[r] in char:
                if len(temp) > len(new):
                    new = temp
                temp = ""
                l += 1
                r = l + 1
            else:
                temp += s[r]
                char[s[r]] = 1
                r += 1
        
        if len(temp) > len(new):
            new = temp
        if new != "":
            return len(new)
        return 0
                
                
            
