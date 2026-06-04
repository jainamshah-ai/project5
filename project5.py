#Class person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("\nPerson Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


#Class Employee
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


#Class Manager
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_details(self):
        print("\nManager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")


#Main
def main():
    person = None
    employee = None
    manager = None

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))

            person = Person(name, age)

            print(
                f"\nPerson created with name: {name} and age: {age}."
            )

        elif choice == "2":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(name, age, employee_id, salary)

            print(
                f"\nEmployee created with name: {name}, age: {age}, "
                f"ID: {employee_id}, and salary: ${salary}."
            )

        elif choice == "3":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            manager = Manager(
                name, age, employee_id, salary, department
            )

            print(
                f"\nManager created with name: {name}, age: {age}, "
                f"ID: {employee_id}, salary: ${salary}, "
                f"and department: {department}."
            )

        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                if person:
                    person.display_details()
                else:
                    print("\nNo Person record found.")

            elif sub_choice == "2":
                if employee:
                    employee.display_details()
                else:
                    print("\nNo Employee record found.")

            elif sub_choice == "3":
                if manager:
                    manager.display_details()
                else:
                    print("\nNo Manager record found.")

            else:
                print("\nInvalid choice!")

        elif choice == "5":
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")

        if choice != "5":
            print("\n--- Choose another operation ---")


#
if __name__ == "__main__":
    main()