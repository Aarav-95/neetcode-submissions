class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0] * 26
        l = 0
        f = True
        for i in s1:
            s1_arr[ord(i)-97] += 1
        x = len(s2)
        s1_len = len(s1)
        cur_len = 0
        l_point = 0
        while l < x:
            temp = [0] * 26
            for i in range(26):
                temp[i] = s1_arr[i]
            if temp[ord(s2[l])-97] > 0:
                temp[ord(s2[l])-97] -= 1
                l += 1
                cur_len += 1
                while l < x and cur_len < s1_len:
                    if temp[ord(s2[l])-97] > 0:
                        temp[ord(s2[l])-97] -= 1
                        l += 1
                        cur_len += 1
                        if cur_len == s1_len:
                            return True
                    else:
                        cur_len = 0
                        l_point += 1
                        l = l_point
                        break
                if cur_len == s1_len:
                    return True
            else:
                l_point += 1
                l = l_point
        return False
            


            