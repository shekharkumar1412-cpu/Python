# we use the key to access their corresponding values
# If we try to access the value of a key that doesn't exist, we'll get an error.


student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters
print(student_id[1130])  # error
