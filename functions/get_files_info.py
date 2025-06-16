import os

def get_files_info(working_directory, directory=None):
    try:
        working_directory = os.path.abspath(working_directory)
        directory = os.path.abspath(directory)
        if not directory.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'

        dir_contents = os.listdir(directory)

        buffer = ""
        for dir_elem in dir_contents:
            buffer += f"-  {dir_elem}: file_size={os.path.getsize(os.path.join(directory, dir_elem))}, is_dir={os.path.isdir(os.path.join(directory, dir_elem))}"
            buffer += "\n"
        return buffer
    except Exception as e:
        return f"Error: {e}"


print(get_files_info("calculator/pkg", "tests.py"))

