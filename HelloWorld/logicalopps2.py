# If age is 5 Go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater than 17 say go to college
# Try to complete with 10 or more lines

# Get age and store in age variable
age = eval(input("Enter age: "))

# If age is 5 Go to Kindergarten
if age < 5:
    print("Too young for school")

# Special Output for age 5 \\ if () and ()
elif age == 5:
    print("Go to Kindergarten")

# Ages 6 through 17 goes to grade 1 through 12
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))

# If age is greater than 17 say go to college
else:
    print("Go to college")
