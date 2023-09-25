# Class of Staffs

class Staff:
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def keep_record(self):
        print(f"{self.name} is responsible for keeping record")

    def customer_care(self):
        print(f"{self.name}Interact with customer")


