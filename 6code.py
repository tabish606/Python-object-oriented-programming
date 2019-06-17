#inheritance method
class Employee:
    increament = 1.5
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname= lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary *Employee.increament)

    @classmethod
    def change_increament(cls,amount):
        cls.increament = amount

    @classmethod

    def from_st(cls,emp_str):
        fname,lname,salary = emp_str.split("-")
        return cls(fname,lname,salary)

    @staticmethod

    def is_open(day):
        if (day== 'sunday'):
            return False
        else:
            return True

harry = Employee.from_st("harry-jackson-70000")
#print(harry.salary)                
#print(harry.is_open("monday"))
class programmer(Employee):
    pass
jon = programmer("jon","snow",10000000)

Employee.change_increament(3)
jon.increase()
print(jon.salary)
#jon.increase()
#print(jon.salary)
#jon.change_increament(3)
#print(jon.salary)
