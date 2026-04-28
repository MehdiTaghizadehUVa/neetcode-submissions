class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                val_1 = stack.pop()
                val_2 = stack.pop()
                if t == "+":
                    res = val_2 + val_1
                    stack.append(res)
                elif t == "-":
                    res = val_2 - val_1
                    stack.append(res)
                elif t == "*":
                    res = val_2 * val_1
                    stack.append(res)
                elif t == "/":
                    res = int(float(val_2) / val_1)
                    stack.append(res)
        return stack.pop()