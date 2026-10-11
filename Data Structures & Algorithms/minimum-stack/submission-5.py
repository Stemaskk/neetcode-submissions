class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval.append(min(val, self.minval[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval[-1]
