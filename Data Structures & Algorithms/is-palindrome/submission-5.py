class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        r = len(s)-1
        while f <= r:
            while f < len(s) and s[f].isalnum() == False:
                f += 1
            while r > -1 and s[r].isalnum() == False:
                r -= 1
            if f < len(s) and r > -1 and s[f].lower() != s[r].lower():
                return False
            f += 1
            r -= 1
        return True
 