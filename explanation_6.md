I am using set to collect the unique elements in both linked lists for both the union and intersection functions.
For both functions, I decided to loop through each list independently so as not to double the time complexity by nesting which is also possible.

The time efficiency for this code is O(n) due to the loops that are directly affected by the size of the inputs.

The space complexity for both union and intersection functions can be calculated as:
    1. size of a node is equals to the size of value(integer of 4 byte)
    2. A set of size n as it depends on size of both input linkedlists that contain integers => 4n
    3. and also a linkedlist is the return value that will contain als0 integers => 4n
    4. Therefore the total space complexity is => O(4n + 4n + 4) ===> O(n)
