# #  --->>>Overloading + Operator For Custom Objects

# class Book:
#     def __init__(self,pages):
#         self.pages=pages

# # creating two objects
# b1=Book(400)
# b2=Book(300)

# # add two objects
# print(b1 + b2)

# # OUTPUT := unsupported operand type(s) for +: 'Book' and 'Book'





# --->>> Same Upper Question

# class Book:
#     def __init__ (self,pages):
#         self.pages=pages
#     # overloading + operator with magic method 
#     def __add__(self,other):
#         return self.pages+other.pages

# b1=Book(400)
# b2=Book(300)
# print(F"Total number of pages: {b1+b2}")




# ===>>>> Overloading The Operator 

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def __mul__(self,timesheet):
#         print(f"Worked for {timesheet.days} days")
#         # calculate salary
#         return self.salary*timesheet.days

# class Timesheet:
#     def __init__ (self,name,days):
#         self.name=name
#         self.days=days

# obj_emp=Employee("Rajan",800)
# obj_time_sheet=Timesheet('Rajan',50)
# print(f"salary is: {obj_emp * obj_time_sheet}")

