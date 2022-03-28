# Helper class to deal with collision cases where will have linkedlist in case different keys generate same index
class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LRU_Cache(object):

    def __init__(self):
        # Initialize class variables
        self.cache = [None for _ in range(5)]
        # List used as a queue to figure out the least used element in the cache
        self.checker = []
        self.size = 0
        self.capacity = 5
        # Use dictionary to store the key, value pairs...and then use a list thats using FIFO to track oldest element
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        return self.cache[key]
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        hash_index = self.get_hash_code(key)
        self.size += 1
        # Find the head element at the index in case there is already a linkedlist there with key,value pairs
        head = self.cache[hash_index]
        while head is not None:
            if head.key == key:
                head.key = value
                return
            head = head.next
        new_node = LinkedListNode(key, value)
        head = self.cache[hash_index]
        new_node.next = head
        self.cache[hash_index] = head
        pass

    def rehash(self):

        pass

    def get_hash_code(self, key):
        return key % self.capacity

    # Helper method for printing out the LRU cache for debugging purposes
    def __repr__(self):
        pass

our_cache = LRU_Cache()

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)


# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5) 
# our_cache.set(6, 6)

# our_cache.get(3)   

