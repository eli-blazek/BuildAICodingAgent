# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

print("Case 1:\n---------------------------")
print(get_files_info("calculator", ".")) # Should pass
print("Should pass")
print("Case 2:\n---------------------------")
print(get_files_info("calculator", "pkg")) # Should pass
print("Should pass")
print("Case 3:\n---------------------------")
print(get_files_info("calculator", "/bin")) # Should print err string
print("Should fail")
print("Case 4:\n---------------------------")
print(get_files_info("calculator", "../")) # Should print err string
print("Should fail")
print("Case 5:\n---------------------------")
print(get_files_info("calculator", "tests.py")) # Should print err string
print("Should fail")