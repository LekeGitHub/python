# temp is a temporary placeholder

course_list = ["Comp_sci", "History", "AI"]

temp = course_list[0]

course_list[0] = course_list[2]

course_list[2] = temp

print(course_list)