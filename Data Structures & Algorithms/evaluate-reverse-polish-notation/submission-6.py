class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                val_1 = stack.pop()
                val_2 = stack.pop()
                res = val_2 + val_1
                stack.append(res)
            elif t == "-":
                val_1 = stack.pop()
                val_2 = stack.pop()
                res = val_2 - val_1
                stack.append(res)
            elif t == "*":
                val_1 = stack.pop()
                val_2 = stack.pop()
                res = val_2 * val_1
                stack.append(res)
            elif t == "/":
                val_1 = stack.pop()
                val_2 = stack.pop()
                res = int(float(val_2) / val_1)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack.pop()