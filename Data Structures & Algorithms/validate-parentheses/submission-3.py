class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        idx = -1
        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
                idx += 1
            else:
                if idx < 0:
                    return False
                if i == ")" and stack[idx] != "(":
                    return False
                if i == "}" and stack[idx] != "{":
                    return False
                if i == "]" and stack[idx] != "[":
                    return False
                stack.pop()
                idx -= 1
                
        if idx > -1:
            return False
        return True
