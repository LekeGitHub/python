# Create Class and make use of conditon in our code

class Employee:
    created_emp = 0
    def __init__(self, first_name, last_name, age, gender, level):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.level = level

        Employee.created_emp += 1


    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def email(self):
        return (f"{self.first_name}{self.last_name}@company.com").lower()



    def staff_payment(self):
        if self.level <= 6:
            print("Salary is $20,000")
        elif self.level > 6 and self.level < 7:
            print("Salary is $30,000")
        elif self.level >= 7 and self.level <= 9:
            print("Salary is $40,000")
        else:
            print("Not yet confirm as a staff of the company")



emp1 = Employee("Morife", "Okusaga", 13, "female", 8)
emp2 = Employee("Oluwatobiloba", "Okusaga", 12, "male", 7)
emp3 = Employee("Arella", "Okusaga", 9, "female", 6)

emp1.staff_payment()

print(Employee.created_emp)
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
print(emp3.fullname())

print(Employee.email(emp3))



