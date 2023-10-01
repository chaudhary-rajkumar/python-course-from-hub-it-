# Example: Creating Class and Object in Python

# class Employee:
#     company_name='ABC Company'

#     # Constructor to initialize the object
#     def __init__(self,name,salary):
#         # instance variables
#         self.name=name
#         self.salary=salary
        
#         # instance method
#     def show(self):
#         print(f"Employee {self.name} {self.salary} {self.company_name}")

# # create first object
# emp1=Employee('Harry', 12000)
# emp1.show()

# # create second object
# emp2=Employee('Raju',11000)
# emp2.show()




# ==>>NOTE Create a Constructor in Python
# class Student:
#     # initialize instance varible in constructor 
#     def __init__(self, name):
#         print("Inside Constructor")
#         self.name=name
#         print("All Variable initialized ")
    
#     # instance method 
#     def show(self):
#         print(f"hello my name is {self.name}")

# # creating object 
# s1=Student('name')
# s1.show()



# NOTE [1] Default Constructor 
# class Employee:
#     def display(self):
#         print("Inside Display")
# emp=Employee()
# emp.display()




# # Non_Parametrized Constructor 

# class Company:
#     # non-argument constructor
#     def __init__(self):
#         self.name='Rajkumar'
#         self.address='Dhakdhai'
    
#     # A Method for printing data members 
#     def show(self):
#         print(f"Name is: {self.name} and Address is {self.address}")

# # creating object of the class 
# cmp=Company()

# # calling the instance method using the object 
# cmp.show()





# # NOTE [2] Parametrized Constructor 
# class Employee:
#     # parametrized constructor 
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     # display object
#     def show(self):
#         print(self.name, self.age, self.salary)
# # creating object of the Employee Class
# rajan=Employee('Rajan',21,75000)
# rajan.show()

# warish=Employee('Warish',22,85000)
# warish.show()





# # ==>> Constructors With Default Values 

# class Student:
#     def __init__(self,name,age=12,classroom=7):
#         self.name=name
#         self.age=age
#         self.classroom=classroom

#     # display student
#     def show(self):
#         print(f"name is {self.name} age is {self.age} class is {self.classroom}")

# # creating object of the student class 
# emma=Student('kelly')
# emma.show()

# kelly=Student('kelly',14)
# kelly.show()




# # ==>> Self Keyword in Python 
# class Student:
#     # constructor 
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     # self points to the current objects
#     def show(self):
#         # access instance variable using self
#         print(f"name: {self.name} age: {self.age}")

# obj=Student('Spiderman',16)
# obj.show()





# ==>> Constructor Overloading
# ==>> Note:- Python does not support constructor overloading






# ==>> Constructor Chaining 

# class Vehicle:
#     def __init__ (self,engine):
#         print('Inside Vehicle Constructor ')
#         self.engine=engine

# class Car(Vehicle):
#     def __init__(self, engine,max_speed):
#         super().__init__(engine)
#         print("Inside car constructor ")
#         self.max_speed= max_speed

# class Electric_Car(Car):
#     def __init__(self, engine, max_speed,km_range):
#         super().__init__(engine, max_speed)
#         print('Inside Electric car constructor')
#         self.km_range=km_range

# # Object of electric car
# ev = Electric_Car('1500cc', 240 , 750)
# print(f"Engine = {ev.engine} Max Speed ={ev.max_speed} km range={ev.km_range}")






# # ==>> Counting The Number Of Objects Of A Class
# class Employee: 
#     count=0
#     def __init__(self):
#         Employee.count=Employee.count+1

# # creating objects
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# print(f"The number of Employee: {Employee.count}")





# Constructor Return Value 
# class Test:
#     def __init__(self,i):
#         self.i=i
#         print(i)
#         # return i
# d=Test(10)

















# NOTE ===>>> Destructor in Python?
# ANS :- It is a special method that is called when an object gets destroyed. On the other hand, a constructor is used to create and initialize an object of a class.

# Synatx of destructor declaratiion
# def __del__(self):
#     # body of a destructor



# Example of destructor:
# class Student:
#     #constructor
#     def __init__(self,name):
#         print("Inside Constructor")
#         self.name=name
#         print('Object initialized')
    
#     def show(self):
#         print(f"Hello, my name is {self.name}")
    
#     # destructor
#     def __del__(self):
#         print('Inside destructor')
#         print('Object destroyed')

# # create object 
# s1=Student('Emma')
# s1.show()

# # delete object
# del s1






# Example of destructor
# import time
# class Student:
#     # constructor
#     def __init__(self,name):
#         print('Inside Constructor ')
#         self.name=name
    
#     def show(self):
#         print(f"Hello , my name is {self.name} \n")
    
#     # destructor 
#     def __del__(self):
#         print('Object Destroyed ')

# s1=Student('Emma')
# s2=s1
# s1.show()

# # delete object reference s1
# del s1

# # add sleep and observe the output
# time.sleep(5)
# print("After sleep ")
# s2.show()





# NOTE Cases When Destructor doesn't work Correctly
# NOTE CASE1==>> Circular Referencing
# NOTE CASE2==>> Exception in __init__ Method 

# Circular Referencing 
# import time
# class Vehicle():
#     def __init__(self,id,car):
#         self.id=id
#         self.dealer=car
#         print(f"Vehicle is {self.id} Created")

#     def __del__ (self):
#         print(f"Vehicle is {self.id} destroyed ")
    
# class Car():
#     def __init__(self,id):
#         self.id=id
#         # saving vehicle class object in dealer vehicle 
#         # sending referencing of Car object ('sefl') for vehicle object 
#         self.dealer=Vehicle(id,self)
#         print(f"Car {self.id} is Created")
    
#     def __del__(self):
#         print(f"car {self.id} is Destroyed")

# c=Car(12)

# time.sleep(3)





# Exception in __init__ method
# class Vehicle:
#     def __init__(self,speed):
#         if speed>240:
#             raise Exception("Not Allowed ")
#         self.speed=speed
    
#     def __del__(self):
#         print("Release resources")

# # Creating an object
# car = Vehicle(550)
# # to delete the object explicity
# del car

















# NOTE ***ENCAPSULATION***

# Example
# class Employee:
#     def __init__(self,name,salary,project):
#         # data members
#         self.name=name
#         self.salary=salary
#         self.project=project

#     # methods to display employee's details
#     def show(self):
#         print(f"Name is {self.name} And salary is {self.salary}")
#     # method
#     def work(self):
#         print(f"{self.name} is working on {self.project}")
    
# # creating object of a class 
# emp=Employee('jessa', 15000,'NPL')

# # calling public method of the class 
# emp.show()
# emp.work()




# Public Members

# class Employee:
#     # constructor 
#     def __init__(self,name,salary):
#         # public data members
#         self.name=name
#         self.salary=salary

#     # public instance methods
#     def show(self):
#         print(f"Name  {self.name} salary {self.salary}")

# emp=Employee('Rajkumar', '15000')

# # accessing public data members
# print(f"Name: {emp.name} Salary: {emp.salary} ")
# emp.show()





