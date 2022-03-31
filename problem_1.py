# Helper class to deal with collision cases where will have linkedlist in case different keys generate same index
class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LRU_Cache(object):

    def __init__(self):
        # List that will be used as the hash map
        self.cache = [None for _ in range(5)]
        # List used as a queue to figure out the least used element in the cache
        self.queue = []
        self.num_entries = 0
        self.capacity = 5
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        hash_index = self.get_hash_code(key)
        head = self.cache[hash_index]
        while head is not None:
            if head.key == key:
                self.queue.pop(0)
                value = head.value
                # Set the value again back in cache to get it later if needed
                self.set(key, value)
                return value
            head = head.next
        return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if not isinstance(key, int) or not isinstance(value, int):
            print("key {} and value {} must be integers".format(key, value))
            return 
        if key < 0:
            print("key should not be a negative integer")
            return 
        hash_index = self.get_hash_code(key)
        # Find the head element at the index in case there is already a linkedlist there with key,value pairs
        if self.num_entries > self.capacity:
            least_used = self.queue.pop(0)
            self.remove_least_used(least_used)
        # Add new key to queue for tracking of least used element
        self.queue.append(key)
        head = self.cache[hash_index]
        while head is not None:
            if head.key == key:
                head.key = value
                return
            head = head.next
        # If we dont find the key above, we either have a new index or a collision happening, hence need to use a linkedlist to solve it
        new_node = LinkedListNode(key, value)
        head = self.cache[hash_index]
        new_node.next = head
        self.cache[hash_index] = new_node
        # Moved count of entries to last place so that its increased only when there is new element in cache
        self.num_entries += 1

    def remove_least_used(self, key):
        # print(key)
        hash_index = self.get_hash_code(key)
        head = self.cache[hash_index]
        while head is not None:
            if head.key == key:
                new_head = head.next
                self.cache[hash_index] = new_head
                self.num_entries -= 1
                return

        pass

    # Simple hash function for generating cache index
    def get_hash_code(self, key):
        return key % self.capacity

our_cache = LRU_Cache()

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       
# returns 1
print(our_cache.get(2))       
# returns 2
print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3)) 
# returns -1 since 3 is the least used cache element  

# Edge case adding null value to cache
print(our_cache.set(None, None))

# Edge case with a negative key 
print(our_cache.set(-1, 7))

# Edge case getting the same value three times
print(our_cache.get(5)) 
print(our_cache.get(5)) 
print(our_cache.get(5)) 