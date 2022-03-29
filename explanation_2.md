The os.listdir() function returns a list, hence making easy choice to decide which data structure to use.

There depth of the directory can be assumed to be n, meaning that the recursive call will be called n times before hitting the last directory.However,
the recursive call is happening within the loop for each item in the directory, meaning thats its a nested loop, hence leading to a time complexity of O(n^2)

For space complexity we have two strings as inputs. Adding to this, there is the loop on the directory list, which contains string values of folders/files inside the directory. Assuming the size of the directory to be n, the space complexity can be calculated as O(n). This is because in worst case scenario the directory list will be larger in size compared to the inputs size, hence their impact is omitted.