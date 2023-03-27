import os 
import json

# Creates a full dictionary of all folder to files
def create_dict(path):
    dir_dict = {}
    # Traverse the directory tree starting from the given path
    for root, dirs, files in os.walk(path):
        # Set the current directory to the root of the dictionary
        curr_dir = dir_dict
        # Get the relative path of the current directory from the root directory
        rel_path = os.path.relpath(root, path)
        # Split the relative path into its component directory names
        dir_names = rel_path.split(os.sep)
        # Traverse the directory tree to the current directory
        for name in dir_names:
            # If the directory name is not already in the current directory, add it
            if name not in curr_dir:
                curr_dir[name] = {}
            # Set the current directory to the directory just added
            curr_dir = curr_dir[name]
        # If there are any files in the current directory, add them to the directory dictionary
        if files:
            curr_dir["Files"] = files
    return dir_dict
