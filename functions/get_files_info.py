import os
from weakref import ref

def get_files_info(working_directory, directory="."):

    if (directory == ".") or (directory == "./"):
        print(f"Results for current directory:")
    else:
        print(f"Results for {directory} directory:")

    
    # Check if the directory is valid and within the working directory
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"Directory '{target_dir}' does not exist.")
    if not os.path.isdir(target_dir):
        raise NotADirectoryError(f"'{target_dir}' is not a directory.")

    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        
    for root, dirs, files in os.walk(target_dir):
        # Process Directories
        for d in dirs:
            dir_path = os.path.join(root, d)
            # Note: getsize on a dir is just the metadata size
            print(f"{d}: size={os.path.getsize(dir_path)}, is_dir=True")
            
        # Process Files
        for f in files:
            file_path = os.path.join(root, f)
            print(f"{f}: size={os.path.getsize(file_path)}, is_dir=False")
    print()

    return 0
    