I am using a list as a bucket for the cache so that I can be able to store the key, value pairs at a specific index that will be determined by the hash function.

Since accessing an item from a list using index i.e. list[idx] uses constant time and the size of the cache is also constant the time complexity is O(1)

The size of the inputs constant i.e. 4 bytes for key and value as they integers, and the bucket cache is also of integer type with the length of 5, meaning that its space complexity is 5n. But since the size of the cache will always remain to be 5 we can summarize space complexity to O(1)

I am also making an assumption that the key, value pairs will be placed and accessed in the same order, hence the reason to use a list as a queue to track the least used element utilising the first in first out characteristics of a queue, hence maintaining constant time and space complexity.