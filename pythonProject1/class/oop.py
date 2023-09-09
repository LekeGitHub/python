# Python Object-oriented programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Adetoroye", "Oluleke", 100000)
emp_2 = Employee("Adetoroye", "Olushola", 90000)

# print(emp_2)
# print(emp_1)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())