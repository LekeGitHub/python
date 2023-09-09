#IF BIRTHDAY IS IMPORTANT OR NOT

# We'll provide different output based on age
# from age 1 - 18 -> important
# 21, 50, > 65 -> Very Important
# All others -> Not Important

# Receive age and store in age
age = eval(input("Enter age: "))

# and : checks if both conditions are true it returns true
# or : checks if either condition are true then true
# not : Converts a true condition into a false

# if age is 1 to 18 = Very Important Birthday
if (age >= 1) and (age <= 18):
    print("Very Important Birthday")

# if age is either 21 or 50 Important
elif (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65 and the convert true to false and vise versa
elif not(age < 65):
    print("Important Birthday")

# Else Not important
else:
    print("Sorry, Not Important Birthday")
