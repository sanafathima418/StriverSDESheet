class StockSpanner:
    
    # Approach: Use mono stack to store price,span for every step
    # TC: O(n)
    # SC: O(n)

    def __init__(self):
        self.mono_stack = []

    def next(self, price: int) -> int:
        # 1. Initialize span to 1 by default so it can be added upon if span extends
        span = 1
        # 2. Pop Condition: If price is greater than top of mono stack
        while(self.mono_stack and price >= self.mono_stack[-1][0]):
            popped_ele = self.mono_stack.pop()
            # 3. Extend span
            span += popped_ele[1]
        # 4. Push to mono stack
        self.mono_stack.append((price,span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)