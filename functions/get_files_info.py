import os

def get_files_info(working_directory, directory = None):
    ### Pre-check
    wd_path_check = os.path.normpath(os.path.abspath(working_directory))
    cd_path_check = os.path.normpath(os.path.abspath(working_directory))
    
    ### Prep path to reasonable format
    if directory is not None:
        full_path_wd = os.path.abspath(os.path.join(working_directory, directory))
    else:
        full_path_wd = os.path.abspath(working_directory)
    full_path_wd = os.path.normpath(full_path_wd)
    
    ### Check if dir is part of workdir and is not a file
    if not full_path_wd.startswith(wd_path_check):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path_wd):
        return f'Error: "{directory}" is not a directory'

    ### Pretty print directory content
    dir_contents = os.listdir(full_path_wd)
    dir_string = ""
    
    for item in dir_contents:
        item_path = os.path.join(full_path_wd, item)
        dir_string += f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n'
    
    return dir_string