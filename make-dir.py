import os
from os import path

out_path = path.abspath(path.join("..", "test_file"))
if not path.exists(out_path):
    os.makedirs(out_path)
for i in range(1, 11):
    os.makedirs(path.join(out_path, "a" + str(i)))
    if i % 2 == 0:
        even_folders = "a" + str(i)
        with open(path.join(out_path, even_folders, "file.text"), "w", encoding="utf-8") as file:
            file.write(even_folders)
