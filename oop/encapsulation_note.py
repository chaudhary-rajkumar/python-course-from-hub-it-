
# encapsulation ::-->>> means building data and methods within a single unit.

# we can do encapsulation by using access modifier

# 1. public member :-->> can be access anywhere from outside of the class.
# 2. protected member :-->> accessible within the class and its sub-class 
# 3. private member :-->> accessible within class and its function only





# --->>> Use Of Public Member

# class Employee:
#     # constructor
#     def __init__(self,name,salary):
#         # public data member
#         self.name=name
#         self.salary=salary

#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")

# emp=Employee('jessa',10000)
# print(f"Name={emp.name} salary={emp.salary}")
# emp.show()





# --->>> Use Of Private Member

# class Employee:
#     # constructor
#     def __init__(self,name,salary):
#         # public data member
#         self.name=name
#         # private data member
#         self.__salary=salary
#     def show(self):
#         print(f"name is {self.name}")

# emp=Employee('jessa',10000)
# print(f"name is {emp.name}")
# print(f"salary is {emp.__salary}") # This line gives error in the program due lo private member can not be access from the outside of the class





# --->>> Public method to access private members

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary

#     # public instance methods
#     def show(self):
#         print(f"name is {self.name} and salary is {self.__salary}")
# emp=Employee('jessa',10000)
# emp.show()






# --->>> Name Mangling Method To Access Private Members

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary

# emp=Employee('jessa',10000)
# print(f"name is {emp.name}")
# # Name Mangling method
# print(f"salary is {emp._Employee__salary}")







# --->>> Protected Member

# # base class 
# class Company:
#     def __init__(self):
#         self._project='NPL'
# # child class
# class Employee(Company):
#     def __init__(self,name):
#         self.name=name
#         Company.__init__(self)

#     def show(self):
#         print(f"Employee name is {self.name}")
#     # accessing data member in child class 
#         print(f"working on project {self._project}")

# c=Employee('jessa')
# c.show()
# # Direct access protected data member
# print(f"your porject is {c._project}")


