class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        count = 0
        lives = k
        temp = 1
        while (r < len(s)):
            if s[r] != s[l]:
                if lives > 0:
                    lives -= 1
                    temp += 1
                    r += 1
                else:
                    if temp > count:
                        if lives > 0 and temp < len(s):
                            temp += 1
                        count = temp 
                    temp = 1
                    lives = k
                    l += 1
                    r = l + 1
            else:
                temp += 1
                r += 1

        if temp > count:
            if lives > 0 and temp < len(s):
                temp += 1
            count = temp
        
        l = len(s)-1
        r = l - 1
        lives = k
        temp = 1
        while (r > -1):
            if s[r] != s[l]:
                if lives > 0:
                    lives -= 1
                    temp += 1
                    r -= 1
                else:
                    if temp > count:
                        if lives > 0 and temp < len(s):
                            temp += 1
                        count = temp
                    temp = 1
                    lives = k
                    l -= 1
                    r = l - 1
            else:
                temp += 1
                r -= 1
            
        if temp > count:
            if lives > 0 and temp < len(s):
                temp += 1
            count = temp
        return count

            
        
