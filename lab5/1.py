# #1
# import re
# text = "row.txt" 
# with open(text, 'r', encoding="utf-8") as file: 
#     string = file.read().strip()
# pattern = r'ab*'
# result = re.findall(pattern, string)
# if result:
#     print(result)
# else:
#     print("Not found")

# #2
# import re
# text = "row.txt"
# with open(text, 'r') as file:
#     string = file.read().strip()
# pattern = r'ab[2-3]'
# result = re.findall(pattern, string)
# if result:
#     print(result)
# else:
#     print("Not found") 

# #3
# import re
# text = "row.txt"
# with open(text, 'r') as file:
#     string = file.read().strip()
# pattern = "\b[a-z]+_[a-z]+\b"
# result = re.findall(pattern, string)
# if result:
#     print(result)
# else:
#     print("Not found") 

# #4
# import re
# text = "row.txt"
# with open(text, "r") as file:
#     string = file.read().strip()
# pattern = "[A-Z][a-z]"
# result = re.findall(pattern, string)
# if result:
#     print(result)
# else:
#     print("Not found") 

# #5
# import re
# text = "row.txt"
# with open(text, "r") as file:
#     string = file.read().strip()
# pattern = "^a.*b$"
# result = re.findall(pattern, string)
# if result:
#     print(result)
# else:
#     print("Not found") 

# #6
# import re
# def replace_characters(text):
#     pattern = r'[ ,\.]'
#     new_text = re.sub(pattern, ':', text)
#     return new_text
# input_text = "Hello, world. How are you doing today?"
# result = replace_characters(input_text)
# print("Result:", result)

# #7
# def snake_to_camel(snake_str):
#     parts = snake_str.split('_')
#     camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:])
#     return camel_case
# snake_string =str(input())
# camel_string = snake_to_camel(snake_string)
# print("Snake case:", snake_string)
# print("Camel case:", camel_string)

# #8
# import re
# def split_at_uppercase(s):
#     parts = re.split(r'(?=[A-Z])', s)
#     parts = [part for part in parts if part]
#     return parts
# input_string =str(input())
# result = split_at_uppercase(input_string)
# print("Original string:", input_string)
# print("Split parts:", result)

# #9
# import re
# def insert_spaces(text):
#     result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
#     return result
# input_text = str(input())
# output_text = insert_spaces(input_text)
# print("Original:", input_text)
# print("Modified:", output_text)

# #10
# import re
# def camel_to_snake(camel_str):
#     snake_str = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', camel_str)
#     return snake_str.lower()
# camel_string = str(input())
# snake_string = camel_to_snake(camel_string)
# print("Camel case:", camel_string)
# print("Snake case:", snake_string)