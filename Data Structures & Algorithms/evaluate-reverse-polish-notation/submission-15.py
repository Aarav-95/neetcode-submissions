class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for i in range(0, len(tokens)):
            if tokens[i] == ops[0]:
                temp = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif tokens[i] == ops[1]:
                temp = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif tokens[i] == ops[2]:
                temp = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif tokens[i] == ops[3]:
                temp = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(int(tokens[i]))
            print(stack)
        return stack[-1]