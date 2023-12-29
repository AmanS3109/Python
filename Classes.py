class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = salary
        self.email = firstname + '.' + '09' + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.salary = int(self.salary * 1.04)


emp_1 = Employee('Aman', 'Singh', 21, 100000)
emp_2 = Employee('Shruti', 'Singh', 20, 100000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)
