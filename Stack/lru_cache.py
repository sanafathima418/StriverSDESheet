class LRUCache:

# Approach: Use stack and hashmap, keep updating stack as and when a key is accessed
# TC: O(1) for get and put functions
# SC: O(1) + O(1) as capacity of cache and stack are constant

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.stack = [] 
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hash_map:
            # If key exists, return and update stack
            self.stack.remove(key)  # Remove key
            self.stack.append(key)  # Append to top of stack
            return self.hash_map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if not key in self.hash_map:
            # Adding new entry so need to check cache capacity 
            if len(self.stack) >= self.capacity:
                # evict key and value
                del_key = self.stack.pop(0)
                del self.hash_map[del_key]
        else:
            # Updating existing entry so need to remove from stack
            self.stack.remove(key)
        self.hash_map[key] = value  # Add/ Update key
        self.stack.append(key)  # Append to top of stack

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)