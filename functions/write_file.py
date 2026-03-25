import os

def write_file(working_directory, file_path, content):

    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    valid_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_path:
        raise ValueError(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    if not os.path.exists(os.path.dirname(target_file)):
        raise FileNotFoundError(f"Error: Directory '{os.path.dirname(target_file)}' does not exist.")
    if os.path.isdir(target_file):
        raise FileNotFoundError(f'Error: Cannot write to "{file_path}" as it is a directory')
    
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    
    with open(target_file, 'w') as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'