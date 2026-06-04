# README.md

## Employee Management System (Python OOP Project)

### Project Overview

This project is a simple **Employee Management System** developed in Python using **Object-Oriented Programming (OOP)** concepts. It demonstrates the use of **Inheritance**, **Method Overriding**, **Classes**, and **Objects**.

The program allows users to:

* Create a Person
* Create an Employee
* Create a Manager
* Display details of created records
* Exit the system through a menu-driven interface

---

## Features

### 1. Person Class

Stores:

* Name
* Age

Methods:

* `display_details()` – Displays person information.

### 2. Employee Class

Inherits from the `Person` class.

Additional attributes:

* Employee ID
* Salary

Methods:

* `display_details()` – Displays employee information.

### 3. Manager Class

Inherits from the `Employee` class.

Additional attribute:

* Department

Methods:

* `display_details()` – Displays manager information.

---

## OOP Concepts Used

### Inheritance

```python
Person → Employee → Manager
```

### Method Overriding

Each class overrides the `display_details()` method to display its own information.

### Encapsulation

Data is stored within objects and accessed through class methods.

---

## Program Menu

```text
--- Python OOP Project: Employee Management System ---

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

---

## Requirements

* Python 3.x

No external libraries are required.

---

## How to Run

1. Save the file as `project5.py`
2. Open Terminal or Command Prompt.
3. Navigate to the project folder.
4. Run:

```bash
python project5.py
```

---

## Example Output

```text
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 2

Enter Name: John
Enter Age: 30
Enter Employee ID: EMP101
Enter Salary: 50000

Employee created with name: John, age: 30, ID: EMP101, and salary: $50000.
```

---

## Learning Outcomes

This project helps in understanding:

* Class creation
* Object instantiation
* Inheritance
* Method overriding
* Constructor chaining using `super()`
* Menu-driven programs in Python
* Basic Employee Management System implementation

---

## Author

**Jainam Work**
Python OOP Project – Employee Management System

---

## Future Enhancements

* Store multiple employees and managers using lists.
* Add search functionality.
* Update employee details.
* Delete employee records.
* Save records to a file or database.
* Implement exception handling for invalid inputs.
