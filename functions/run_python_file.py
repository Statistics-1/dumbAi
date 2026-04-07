import os 
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:

        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs,file_path))

        valid_path = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if not valid_path:
            raise ValueError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file):
            raise FileNotFoundError(f'Error: "{file_path}" does not exist or is not a regular file')
        if not target_file.endswith('.py'):
            raise ValueError(f'Error: "{file_path}" is not a Python file')
        
        absolute_file_path = os.path.abspath(file_path)
        command = ["python", absolute_file_path]
        command.extend(args)

        result = subprocess.run(command, cwd=os.path.dirname(absolute_file_path),capture_output=True, text=True, timeout=30)


        output = ""  
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        
        if not (result.stdout or result.stderr):
            output += 'No output produced'
        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}"
        
        return output
    except Exception as e:
        return e
