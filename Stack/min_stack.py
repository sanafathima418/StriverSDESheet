class MinStack:
# Approach 1: Stack of Value/ Minimum Pairs
# Alternate Approach: Can use 2 stack to achieve the same
# TC: O(1) for all functions
# SC: O(N) for the min stack

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append((val,val))
        else:
            min_ele = min(val, self.min_stack[-1][1])
            self.min_stack.append((val,min_ele))

    def pop(self) -> None:
        if self.min_stack:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()