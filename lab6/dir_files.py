# #1
# import os
# path = input("Enter the directory path: ")
# if os.path.exists(path):
#     items = os.listdir(path)
#     print("Directories:")
#     for item in items:
#         if os.path.isdir(os.path.join(path, item)):
#             print(item)
#     print("\nFiles:")
#     for item in items:
#         if os.path.isfile(os.path.join(path, item)):
#             print(item)
#     print("\nAll items:")
#     for item in items:
#         print(item)
# else:
#     print("The specified path does not exist!")

# #2    
# import os
# path = str(input("Enter the directory path: "))
# print(os.access(path, os.F_OK)) # Existence
# print(os.access(path, os.R_OK)) # Readability
# print(os.access(path, os.W_OK)) # Writeability
# print(os.access(path, os.X_OK)) # Executeability

# #3
# import os
# path = str(input("Enter the directory path: "))
# if os.access(path, os.F_OK):
#     list = os.listdir(path)
#     print("Files and Folders")
#     for i in list:
#         print(i)
# else:
#     print("path is wrong! ")

# #4
# file_name = 'test.txt'
# file = open(file_name)
# sum = 0 

# for line in file:
#     sum += 1
# print(sum)

# file.close()

# #5
# file_name = 'text.txt'

# file = open(file_name, 'w')

# content = str(input("write content: "))

# file.write(content)

# #6
# import string
# for letter in string.ascii_uppercase:
#         filename = f"{letter}.txt"
#         try:
#             with open(filename, "x") as file:
#                 file.write(f"This is file {filename}\n")
#             print(f"Created file: {filename}")
#         except FileExistsError:
#             print(f"File {filename} already exists. Skipping creation.")

# #7
# filename = input("Filename: ")  

# try:
#     with open(filename, 'r') as orig:
#         content = orig.read()  
#     copy_filename = f"{filename}_copy.txt"  
#     with open(copy_filename, 'w') as copy:
#         copy.write(content)  

#     print(f"File copied successfully as '{copy_filename}'")

# except FileNotFoundError:
#     print(f"Error: The file '{filename}' does not exist.")

#8
import os
filename = str(input("filename: "))
file = filename
if os.access(file, os.F_OK):
    os.remove(file)
else:
    print("file does not exist!")


