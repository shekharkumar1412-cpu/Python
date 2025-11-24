# A file is a container in computer storage devices used for storing data.
# When we want to read from or write to a file, we need to open it first.
# When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:
                        # 1.) Open a file
                        # 2.) Read or write (perform operation)
                        # 3.) Close the file

                    
                    
                                
                                # Opening file
# By default  when we open a file it is in read mode(i.e we can only read the file.)



# file1 = open("msg.txt")      # equivalent to 'r' or 'rt'
# file1 = open("msg.txt",'w')  # write in text mode
# file1 = open("msg.txt",'a')  # append mode

# f = open('msg.txt')          # by default it is in read mode
f=open("msg.txt","r")       # here r is used which denotes that it is in read mode only



# reading the content: After we open a file, we use the read() method to read its contents. 

# content=f.read()
# print(content)

con=f.read(6)
print(con)

more_con=f.read(20)  # reads 20 character from the remaining text in file.
print(more_con)

f.close()

# If an exception occurs when we are performing some operation with the file,
#  the code exits without closing the file. A safer way is to use a try...finally block.

try:
        file1=open('msg.txt')
        content=file1.read()
        print(content)

finally:
        file1.close()


# In Python, we can use the with...open syntax to automatically close the file.
with open("msg.txt", "r") as file1:
    read_content = file1.read()
    print()
    print(' using with...open syntax to print')
    print(read_content)
    print("---------------------------------------")
    c= file1.readable()  # returns true as file1 here is readable
    print(c)
