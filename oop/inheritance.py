class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def details(self):
        print(f" name is {self.name} address is {self.address} and age is {self.age}")

class Employee(Person):
    def __init__(self,name,age,address,department,salary):
        super().__init__(name,age,address)
        self.department=department
        self.salary=salary
    def emp_detail(self):
        print(f" name is {self.name} address is {self.address} and age is {self.age} department is {self.department} and salary is {self.salary}")


# --->>>> object is always pass in child class not in parent class
obj=Employee("Hariram",15,"NEpal","Marketing",25000)

obj.details()
obj.emp_detail()




 
