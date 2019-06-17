class Employee:
    increament = 1.6
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary*Employee.increament)

    @classmethod
    def change_increament(cls,amount):
        cls.increament = amount
    @classmethod

    def from_str(cls,emp_str):
        fname,lname,salary = emp_str.split('-')
        return cls(fname,lname,salary)
harry = Employee.from_str("harry-sharma-9000")        
peter = Employee.from_str("peter-parker-30000")
print(peter.fname)        
print(harry.fname,harry.lname,harry.salary , end = " ")
print(peter.salary)
