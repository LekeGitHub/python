class Employee:

    raise_amount = 1.4
    num_of_employee = 0
    def __init__(self, firstname, lastname, level, age, gender, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.level = level
        self.age = age
        self.pay = pay
        self.gender = gender
        self.email = (firstname + "." + lastname + "@company.com").lower()

        Employee.num_of_employee += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"
        # return '{} {}'.format(self.firstname, self.lastname)

    # def pay(self):
    #     if self.level == 8:
    #         pay = 100000
    #         return pay
    #     elif self.level == 9:
    #         pay = 200000
    #         return pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        pass
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Oluleke", "Adetoroye", 8, 25, "male", 100000)
emp2 = Employee("Tolu", "Adegoke", 9, 27, "female", 200000)

import datetime
my_date = datetime.date(2023, 2, 10)

print(Employee.is_workday(my_date))
# print(emp1.email)
# print(Employee.fullname(emp2))
# print(Employee.fullname(emp1))

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

print("Number of employee created", Employee.num_of_employee)

# Employee.apply_raise(emp2)
# print(emp2.pay)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# print(emp1.__dict__)
# print(Employee.__dict__)