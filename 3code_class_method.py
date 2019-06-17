class Employee:
    increament =1.5
    def __init__(self,fname,lname,salary):
        self.fname =fname
        self.lname = lname
        self.salary = salary
    def increase(self):
        self.salary = int(self.salary*Employee.increament)

    @classmethod
    def change_increament(cls,amount):
        cls.increament = amount       

harry = Employee("harry","sharma",40000)
john = Employee("john","carter",50000)
print(harry.salary)
Employee.change_increament(1.5)
harry.increase()
print(harry.salary)