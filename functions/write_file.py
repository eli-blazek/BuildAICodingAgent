def write_file(working_directory, file_path, content):
    wd_path_check = os.path.normpath(os.path.abspath(working_directory))
    cd_path_check = os.path.normpath(os.path.abspath(file_path))
    
    ### Prep path to reasonable format
    full_path_wd = os.path.abspath(os.path.join(working_directory, file_path))
    
    ### Check if dir is part of workdir and is not a file
    if not full_path_wd.startswith(wd_path_check):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path_wd):
        return f'Error: File not found or is not a regular file: "{file_path}"'
