# python file dectection
import os

file_path = "chapter40-file_detection/test.txt"

if os.path.exists(file_path):
    print(f"The location of the file path is : {file_path}")
    if os.path.isfile(file_path):
        print("This is a file!")
    elif os.path.isdir(file_path):
        print("This is a directory!")
else:
    print("File path does not exist!")
