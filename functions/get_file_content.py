import os

def get_file_content(working_directory, file_path):

    charlimit = 10000

    try:
        
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        if not os.path.exists(target_file):
            raise FileNotFoundError(f"File '{target_file}' does not exist.")
        if not os.path.isfile(target_file):
            raise  FileNotFoundError(f'Error: File not found or is not a regular file: "{file_path}"')
        
        valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if not valid_target_file:
            raise ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
        with open(target_file, 'r') as f:
            content = f.read(charlimit)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {charlimit} characters]'
            return content
    except Exception as e:
        print(e)
        return str(e)


