import glob
import os


directory = "C:/Users/sarap/py_dev/Exercises/subdirs/"
print(directory)

configfiles = glob.glob('C:/Users/sarap/py_dev/Exercises/subdirs/**/*.py', recursive=True)
print(len(configfiles))
