import os

def find_files(suffix, path):
    # Create an empty list container that will hold the results
    files_path = list()
    if suffix != '.c' or not(os.path.isdir(path)):
        return None
    
    #inner recursive function 
    def _find_files(suffix, path):
        curr_directory = os.listdir(path)
        for item in curr_directory:
            print(item)
            new_path = os.path.join(path, item)
            #Check if the file/item is a directory, if yes do a recursive call
            if os.path.isdir(new_path):
                _find_files(suffix, new_path)
            # Otherwise append the file name to the files_path
            if new_path and item.endswith(suffix):
                files_path.append(new_path)
        
    _find_files(suffix, path)
    return files_path
                     

# will print list with correct files found  
print(find_files('.c', '.'))
# Will return None since the extension is incorrect
print(find_files('.txt', '.'))
# Will return None since the path is incorrect
print(find_files('.c', 'path'))