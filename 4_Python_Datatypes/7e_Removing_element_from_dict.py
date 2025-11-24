# We use the del statement to remove an element from the dictionary

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print("Initial Dictionary: ", student_id)

del student_id[111]

print("Updated Dictionary ", student_id)


del student_id
print(student_id)           # Here we have deleted the student_id dictionary and 
#                                        student_id doesn't exist anymore.

