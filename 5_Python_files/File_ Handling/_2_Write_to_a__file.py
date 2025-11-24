# There are two things we need to remember while writing to a file.
        #    If we try to open a file that doesn't exist, a new file is created.
        #    If a file already exists, its content is erased, and new content is added to the file.

# In order to write into a file in Python, we need to open it in write mode
#  by passing "w" inside open() as a second argument.

with open ('test2.txt' , 'w') as file2:
    file2.write("HEllo World!")
    file2.write("Welcome to our world!")    # Here, a new test2.txt file is created and this file
                                             #  will have contents specified inside the write() method.


with open ('test2.txt','w') as file2:      # here test2.txt will be updated by the content
  file2.write("Hi Shekhar")                  # specified here inside write() method.
  
  print(file2.tell())    # returns an int which indicates the current position of files object
  file2.write("How are yoy?")
  print("---------------------------------------")
  c= file2.readable()
  print(c)     # here file is not readable hence returns false
  print(file2.tell())    # returns an int which indicates the current position of files object