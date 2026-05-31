class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""
        count = 0
        def back(i):
            nonlocal cur, count
            if i == 0:
                temp = cur
                while len(temp) < 2*n:
                    temp += ")"
                res.append(temp)
                return
            
            cur += "("
            count += 1
            back(i-1)

            while cur[-1] == ")":
                cur = cur[:len(cur)-1]
                count += 1
            if cur[-1] == "(":
                cur = cur[:len(cur)-1]
                count -= 1
            if count > 0:
                cur += ")"
                count -= 1
                back(i)
        
        back(n)
        return res