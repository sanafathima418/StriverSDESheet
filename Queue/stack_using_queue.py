class MyStack:
    
    # Approach 1: 2 queues (Refer LC solution)
    # Time Complexity: O(N) for push and O(1) for pop
    # Space Complexity: O(N) + O(N) for 2 queues
    
    # Approach 2: 1 queue
    # Time Complexity: O(N) for push and O(1) for pop
    # Space Complexity: O(N) for 1 queue
    # Intuition: Swap elements one by one until last element(newly added) bubbles to front of queue

    def __init__(self):
        self.queue = []
    
    def swap(self,i,j):
        tmp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = tmp

    def push(self, x: int) -> None:
        self.queue.append(x)
        
        # If empty and first insert, no need to bubble to front
        # Else bubble to front
        if len(self.queue) > 1:
            i = len(self.queue)-1
            j = i-1
            while(j > -1):
                self.swap(i,j)
                i -= 1
                j -= 1

    def pop(self) -> int:
        if self.empty():
            return -1
        ele = self.queue[0]
        self.queue.pop(0)
        return ele

    def top(self) -> int:
        if not self.empty():
            return self.queue[0]
        return -1

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()