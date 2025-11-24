                                        # A namespace is a collection of names. 

# In Python, we can imagine a namespace as a mapping of every name we have defined to corresponding objects.

# It is used to store the values of variables and other objects in the program, 
        # and to associate them with a specific name. 

# This allows us to use the same name for different variables or objects in different parts of our code,
        # without causing any conflicts or confusion.

# A namespace containing all the built-in names is created when we start the Python interpreter 
            # and exists as long as the interpreter runs thats why we can use  built-in functions like id(), 
                     # print() etc. anywhere in our program. 

# Different namespaces are isolated. Hence, the same name that may exist in different modules does not collide.

# Modules can have various functions and classes. 

# A local namespace is created when a function is called, which has all the names defined in it.

# (Similar is the case with class)




                                            # Python Variable Scope

# A scope is the portion of a program from where a namespace can be accessed directly without any prefix.

# At any given moment, there are at least three nested scopes.
    # 1. Scope of the current function which has local names
    # 2. Scope of the module which has global names
    # 3. Outermost scope which has built-in 

# When a reference is made inside a function, the name is searched in the local namespace, 
    # then in the global namespace and finally in the built-in namespace

# If there is a function inside another function, a new scope is nested inside the local scope.






    



