class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cmap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        res = []
        n = len(digits)

        if n == 0:
            return []
        def back(i, curr):
            if i >= n:
                res.append(curr)
                return
            
            x = int(digits[i])
            curr += cmap[x][0]
            back(i+1, curr)
            curr = curr[:len(curr)-1]
            
            curr += cmap[x][1]
            back(i+1, curr)
            curr = curr[:len(curr)-1]
            
            curr += cmap[x][2]
            back(i+1, curr)
            curr = curr[:len(curr)-1]

            if x == 7 or x == 9:
                curr += cmap[x][3]
                back(i+1, curr)
                curr = curr[:len(curr)-1]
        
        back(0, "")
        return res