import os 

os.mkdir("New directory created to be renamed ")
print(os.listdir())
print("=================================================================================")
os.rename('New directory created to be renamed','updated name of the new created directory' )
print(os.listdir())
