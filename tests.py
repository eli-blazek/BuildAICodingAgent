# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

print(get_files_info("calculator", ".")) # Should pass
print(get_files_info("calculator", "pkg")) # Should pass
print(get_files_info("calculator", "/bin")) # Should print err string
print(get_files_info("calculator", "../")) # Should print err string