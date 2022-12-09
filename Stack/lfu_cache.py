from collections import defaultdict, OrderedDict

class LFUCache:

# Approach: Use ordereddict and normal dict, keep updating stack as and when a key is accessed
# TC: O(1) for get and put functions as we use ordereddict which works like a DLL
# SC: O(1) + O(1) as capacity of the 2 dicts is constant

    def __init__(self, capacity: int):
        self.value_map = {} # To store all keys and their frequencies (key:freq)
        self.freq_map = {}  # To store all keys and value in cache in order (freq: {key: val})
        self.capacity = capacity
        self.lowest_frequency = 1

    def update_key(self,key: int, value: int = None): 
        freq = self.value_map[key]
        if not value:
            # Get operation being performed so retain val
            val = self.freq_map[freq][key]
        else:
            # Put operation for exisiting key, so update val
            val = value
        # 1. Remove entry from freqmap
        del self.freq_map[freq][key]  
        # 2. Append to front of freqmap
        if freq+1 in self.freq_map:
            self.freq_map[freq+1][key] = val  
        else:
            self.freq_map[freq+1]= defaultdict(OrderedDict)
            self.freq_map[freq+1][key] = val  
        # 3. Update freq in valuemap
        self.value_map[key] = freq+1
            
        if self.lowest_frequency == freq and not self.freq_map[freq]:  # Update lowest freq
            self.lowest_frequency += 1
            
        return val

    def get(self, key: int) -> int:
        if key in self.value_map:
            # If key exists, return and update freq_map and value_map
            return self.update_key(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if not key in self.value_map:
            # Adding new entry so check cache capacity 
            if not self.capacity:
                # Evict key and value
                if self.lowest_frequency in self.freq_map:
                    # 1. Get 1 st key in ordered dict
                    first_key = next(iter(self.freq_map[self.lowest_frequency]))
                    if len(self.freq_map[self.lowest_frequency]) > 1: 
                        # 2. If more than one entry for lowest freq, need to evict as per lru
                        del self.freq_map[self.lowest_frequency][first_key]
                        del self.value_map[first_key]
                    else:
                        # 3. Only one entry for lowest frew so evict directly
                        del self.freq_map[self.lowest_frequency]
                        del self.value_map[first_key]
                    self.capacity += 1
            if self.capacity:
                # To ensure there is any capacity to begin with 
                if 1 not in self.freq_map: # Adding element for first time so freq is 1
                    self.freq_map[1] = defaultdict(OrderedDict)
                self.freq_map[1][key] = value  # Add key in freqmap
                self.value_map[key] = 1 # Add key in valuemap
                self.lowest_frequency = min(1, self.lowest_frequency) # Update lowest freq
                self.capacity -= 1 # Update capacity
        else:
            # Updating existing entry 
            self.update_key(key,value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)