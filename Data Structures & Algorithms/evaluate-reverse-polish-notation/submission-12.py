class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        length = 0
        for i in tokens:
            if i == "+":
                stack[length-2] += stack[length-1]
                stack.pop()
                length -= 1
            elif i == "-":
                stack[length-2] -= stack[length-1]
                stack.pop()
                length -= 1
            elif i == "*":
                stack[length-2] *= stack[length-1]
                stack.pop()
                length -= 1
            elif i == "/":
                stack[length-2] = -(-stack[length-2] // stack[length-1]) if (stack[length-2] < 0) ^ (stack[length-1] < 0) else stack[length-2] // stack[length-1]
                stack.pop()
                length -= 1
            else:
                i = int(i)
                stack.append(i)
                length += 1
            print(stack[length-1])
        return stack[0]