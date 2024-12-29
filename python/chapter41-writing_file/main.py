from logging import exception


txt_data = "I like pizza!"

file_path = "chapter41-writing_file/output.txt"


try:
    with open(file_path, "a") as file:
        file.write("\n"+txt_data)
        print(f"Text path '{file_path}' was created.")
except FileExistsError:
    print("File exists: 'chapter41-writing_file/output.txt'")
