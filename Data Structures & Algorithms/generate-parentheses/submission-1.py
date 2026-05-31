class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""
        count = 0
        def back(i):
            nonlocal cur, count
            print(cur, i, count)
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
            print("-")
            print(cur, i, count)
            print("-")
            if count > 0:
                cur += ")"
                count -= 1
                back(i)
        
        back(n)
        return res