class Employee:
    increament = 1.5
    no_of_employees = 0

    def __init__(self,fname,lname,salary):
        self.fname =fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1
    def increase(self):
        self.salary = int(self.salary*Employee.increament )  
print(Employee.no_of_employees)        
harry = Employee("harry","sharma",40000)
john = Employee("john","carter",50000)
print(Employee.no_of_employees)
print(harry.salary)
harry.increase()
print(harry.salary)
print(john.salary)
john.increase()
print(john.salary)
print(Employee.__dict__)# it will show the all variable of employee class