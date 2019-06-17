class Employee:
    increament = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def increase(self):
        self.salary= int(self.salary*Employee.increament)
    @classmethod
    def change_increament(cls,amount):
        cls.increament = amount
    @classmethod
    def from_str(cls,emp_str):
        fname ,lname, salary = emp_str.split("-")
        return cls(fname,lname,salary)
    @staticmethod 

    def is_open(day):
        if (day == "sunday"):
            return False
        else:
            return True
harry = Employee.from_str("harry-sharma-76000")            
print(Employee.is_open("monday"))                    
print(harry.is_open("sunday"))