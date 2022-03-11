from queue import Queue

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.arr = [None for _ in range(capacity)]
        self.size = 0
        self.coefficient = 31
        # Use dictionary to store the key, value pairs...and then use a list thats using FIFO to track oldest element
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        pass

    def handle_full_capacity(self):

        pass

    def get_hash_code(self, key):
        hash_code = key * self.coefficient % len(self.arr)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)   

