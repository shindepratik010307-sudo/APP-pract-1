class Employee:
    company_name = "TechNova Pvt Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, "earns", self.salary)

    @staticmethod
    def is_high_salary(salary):
        return salary >= 50000

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


e1 = Employee("Rahul", 45000)
e2 = Employee("Sneha", 70000)

print(e1.name, e1.salary, e1.company_name)
print(e2.name, e2.salary, e2.company_name)

e1.display()
e2.display()

print(Employee.is_high_salary(40000))
print(Employee.is_high_salary(70000))

print(e1)
print(e2)


def notify(func):
    def wrapper(*args, **kwargs):
        print("Process Started")
        result = func(*args, **kwargs)
        print("Process Completed")
        return result
    return wrapper


@notify
def check_employee(emp):
    if Employee.is_high_salary(emp.salary):
        print(emp.name, "has High Salary")
    else:
        print(emp.name, "has Normal Salary")


check_employee(e1)
check_employee(e2)


class EmployeeID:
    def __init__(self, total):
        self.total = total

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        if self.current <= self.total:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


print("\nIterator Output:")
for i in EmployeeID(5):
    print("Employee ID:", i)


def employee_ids(total):
    current = 1
    while current <= total:
        yield current
        current += 1


print("\nGenerator Output:")
for i in employee_ids(5):
    print("Employee ID:", i)