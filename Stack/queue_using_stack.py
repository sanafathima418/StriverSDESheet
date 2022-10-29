class MyQueue:
    
    # Approach: 1 queue
    # Time Complexity: O(N) for push and O(1) for pop
    # Space Complexity: O(N) for 1 queue
    # Intuition: Swap elements one by one until last element(newly added) bubbles to front of stack
    # Last element is the open end of stack where pushes and pops happen from

    def __init__(self):
        self.stack = []
        
    def swap(self,i,j):
        tmp = self.stack[i]
        self.stack[i] = self.stack[j]
        self.stack[j] = tmp

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        # If empty and first insert, no need to bubble to front
        # Else bubble to front
        if len(self.stack) > 1:
            i = len(self.stack)-1
            j = i-1
            while(j > -1):
                self.swap(i,j)
                i -= 1
                j -= 1

    def pop(self) -> int:
        if not self.stack:
            return -1
        ele = self.stack[-1]
        self.stack.pop()
        return ele

    def peek(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def empty(self) -> bool:
        if not self.stack:
            return -1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()