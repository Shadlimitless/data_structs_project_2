A node seemed like the best data structure to store the char and their count , and I am create the tree due to its right and left child properties.

Assuming the data size is n , worst case time complexity of the encoding function is O(n) since we have to loop through the data to get each char independently.

For space complexity for encoding function:
    1. I am creating a node of size 5 bytes( 1 char for data and 4 bytes for the frequency)
    2. In the first loop (lines 126), assuming data input size is n , the total size of the list of nodes will be 5n
    3. I am assuming that the summing operation (line 131) will result in same number of nodes plus additional nodes holding the summed frequencies. These nodes will contain the frequency (4 bytes) and two nodes (each 5 bytes). They will be half of the current number since its a sum of two nodes, hence their space complexity will be => 4 + 5 + 5 + log n ==> O(14log n).
    4. There is a dictionary created that holds the char as the key and corresponding node (created in first loop as value). The computational space here is therefore O(n + 5n)
    5. The encoding is a string of bits which is half the size of the data => O(n/2)
    6. total complexity O(5n + 14 log n + n/2) ==> O(n)

For decoding the return size is twice the size of data since data is in bits , hence O(2n) ==> O(n)