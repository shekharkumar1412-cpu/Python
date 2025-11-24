# Taking input by user using input() function

print()

num = input('Enter a number: ')             # Here inputted number is of the str type not of the int type 
print('You Entered:', num)
print('Data type of num:', type(num))


# Converting input number into int type from str type(which is the default datatype of input)

print()

num = int(input('Enter a number: '))
print('You Entered:', num)
print('Data type of num:', type(num))


# Another example
print()

name= input('Enter the user name:')
password= input('Enter the password:')

print("Your user name is:",name)
print(type(name))

print()

print("Your login password is:",password)
print(type(password))