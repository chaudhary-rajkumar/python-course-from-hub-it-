class Company:
    # constructor
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print(f"your name is {self.name} and salary is {self.salary}")

# object
abc=Company('Rupak','14000') 
abc.show()

