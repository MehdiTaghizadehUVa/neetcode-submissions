class MinStack:

    def __init__(self):
        self.stack = []
        self.pre_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.pre_min:
            self.pre_min.append(val)
        else:
            self.pre_min.append(min(self.pre_min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.pre_min.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pre_min[-1]
