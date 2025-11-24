                                              # Syntax
                            #  while condition:
                                        # body of while 


# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1




                # Example 2: Python while Loop to Display Game Level


    current_level = 0
final_level = 5

game_completed = True

while current_level <= final_level:
    if game_completed: 
        print('You have passed level', current_level)
        current_level += 1

print('Level Ends')