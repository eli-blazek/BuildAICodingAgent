import os

# The directory parameter should be treated as a relative path within the working_directory
def get_files_info(working_directory, directory=None):
    wd_contents = os.listdir(working_directory)
    full_path = os.path.join(working_directory, directory)
    
    if directory not in wd_contents:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not (os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    

    