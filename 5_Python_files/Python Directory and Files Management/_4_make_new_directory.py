import os

print("printing current directory:")
print(os.getcwd())
print("===================================")

print("Making a new directory in the current working directory:")
os.mkdir('test')                # created a new folder/directory named inside the current directory
print("-------------------------------")
print("All directory/files in the current working directories")
print(os.listdir())

os.mkdir('D://python//5_Python_files//Python Directory and Files Management//New Directory name ')
# created a new directory named New Diectory name in the directory 
#               D://python//5_Python_files//Python Directory and Files Management