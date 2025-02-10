import os
import pathlib


if os.path.exists('data.txt'):
    print("File exists")
else:
    print("File not found")
# File not found

file_path = pathlib.Path('name.txt')

if file_path.exists():
    print("File is exist")
else:
    print("Not exist")
# File is exist


# to get full path
print(os.path.abspath('name.txt'))
# E:\Full-Stack-Web-Development-with-Python-Django-React\Module 3\0 Prerecord Class\name.txt

# to get size
print(os.path.getsize('name.txt'))
# 194


with open('name.txt', 'r') as f:
    print(f.tell())
# 0


with open('name.txt', 'r') as f:
    print(f.read(5))
# Hello   