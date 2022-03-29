I am using a list to store both groups and users since its easy to iterate through them

The time complexity of the solution is O(n) since there is a loop over the groups which can be assumed to be of n size.

For Space complexity, I'm creating two lists that are made up of strings , or list of strings. We can assume the size of the string/lists to be n. The return is a boolean that is of 1 byte, hence space complexity can be summarized as O(n)