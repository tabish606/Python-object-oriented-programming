class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

harry = Employee("harry","sharma",40000)
john = Employee("john","carter",50000)

print(harry.salary,john.lname)