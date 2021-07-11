import sys
import os

file_path = "/Users/palumbo/Desktop/Test/test2"

split_file_path = file_path.split('/')
# print(split_file_path)

new_split_file_path = split_file_path[: len(split_file_path) - 2]
# print(new_split_file_path)

new_path = '/'
new_path = new_path.join(new_split_file_path)

# print(new_path)

command = "mv " + file_path + " " + new_path

os.system(command)