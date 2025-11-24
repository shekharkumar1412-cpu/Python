import os 

# creating two new directories
os.mkdir("New dir1")
os.mkdir('New dir2')


print("--------------------------------------------------")
print("Before deleting all directories:")
print(os.listdir())
print("------------------------------------------------")

# using  remove() to delete a file,
os.remove("D://python\/5_Python_files\/Python Directory and Files Management//New dir1")

# using rmdir() to delete an empty directory
os.rmdir("D://python\/5_Python_files\/Python Directory and Files Management//New dir2")

print("After deltion left directories are:")
print(os.listdir())
print("----------------------------------------------------------------------")