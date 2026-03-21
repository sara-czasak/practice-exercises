import glob
import os

directory = f"{os.getcwd()}/files_to_sort"
print(directory)
py_count = 0

# My version
for file in glob.glob(f"{directory}/*.py"):
    py_count += 1

print(py_count)

# Ardit's version

file_list = glob.glob1(directory, "*.py")
print(len(file_list))