'''
Each operation is completed in O(1) time
'''
class MinStack:

    def __init__(self):
        self.stack = list()
        self._top = -1
        self.min = 0
        self.minlist = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._top += 1
        if len(self.minlist) > 0:
            val = min(val, self.minlist[-1])
        self.minlist.append(val)

    def pop(self) -> None:
        if self._top >= 0:
            self.minlist.pop()
            self.stack.pop()
            self._top -= 1

    def top(self) -> int:
        if self._top < 0:
            return
        return self.stack[self._top]

    def getMin(self) -> int:
        return self.minlist[-1]

    
minStack = MinStack()
print(minStack.push(1))
print(minStack.push(2))
print(minStack.push(0))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
