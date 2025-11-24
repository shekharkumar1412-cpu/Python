# The escape sequence is used to escape some of the characters present inside a string.
# Suppose we need to include both double quote and single quote inside a string,

# example = "He said, "What's there?""

#Since strings are represented by single or double quotes, 
# the compiler will treat "He said, " as the string. Hence, the above code will cause an error.
# To solve this issue, we use the escape character \ in Python.

# escape double quotes
example = "He said, \"What's there?\""

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)  # Output: He said, "What's there?"




# Here is a list of all the escape sequences supported by Python.

# Escape Sequence	Description
# \\	            Backslash
# \'	            Single quote
# \"	            Double quote
# \a	            ASCII Bell
# \b	            ASCII Backspace
# \f	            ASCII Formfeed
# \n	            ASCII Linefeed
# \r	            ASCII Carriage Return
# \t	            ASCII Horizontal Tab
# \v	            ASCII Vertical Tab
# \ooo	            Character with octal value ooo
# \xHH	            Character with hexadecimal value HH



