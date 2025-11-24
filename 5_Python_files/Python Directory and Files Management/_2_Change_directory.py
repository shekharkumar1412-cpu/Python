import os
print('===============================================')
print("Initial location/directory of the current file is :")
print(os.getcwd())     # prints =>  D:\python\5_Python_files\Python Directory and Files Management
print("-------------------------------------------------------------")

os.chdir("D://python\\5_Python_files")
print('Updated location/directory of the current file is :')
print(os.getcwd())          # prints the updated location/directory of the current file
print()
