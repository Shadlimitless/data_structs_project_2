I am using a list as a bucket for the cache so that I can be able to store the key, value pairs at a specific index that will be determined by the hash function.

Since accessing an item from a list using index i.e. list[idx] uses constant time and the size of the cache is also constant the time complexity is O(1)

The size of the inputs constant i.e. 4 bytes for key and value as they integers, and the capacity of the cache is constantly at 5, not increasing regardless of the inputs since we will be removing least used cache elements. Hence the space complexity is O(1)