The os.listdir() function returns a list, hence making easy choice to decide which data structure to use.

There depth of the directory can be assumed to be n, meaning that the recursive call will be called n times before hitting the last directory, therefore the time complexity can be equated to the depth of the directory O(n)

For space complexity we have two strings as inputs. Adding to this, there is the loop on the directory list, which contains string values of folders/files inside the directory. Assuming the size of the directory to be n, the space complexity can be calculated as O(n). This is because in worst case scenario the directory list will be larger in size compared to the inputs size, hence their impact is omitted.