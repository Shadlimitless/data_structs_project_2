import os

def find_files(suffix, path):
    # Create an empty list container that will hold the results
    files_path = list()
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
                     
print(find_files('.c', '.'))