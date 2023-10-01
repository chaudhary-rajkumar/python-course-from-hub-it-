# ==>>identation error
# print("Welcome to PYnative")
#     print("Learn Python with us..")

# -->> error maded by space or tab in the program is called unexpected indent




# ==>> NameError or Logical errors
# a=10
# b=20
# print(f"Addition is {a+c}")
# -->> due to c name was not defined 





# FileNotFoundError
# fp=open("test.txt","r")
# print(fp)





# # Try And Except Block To Handling Exceptions --->>> syntax
# # try:
# #     statement in try block
# # except:
# #     executed when exception occured in try block





# # ZeroDivisionError
# a=10
# b=0
# c=a/b
# print(f"a / b = {c}")




# # try and except to handle zerodivision error
# try:
#     a=10
#     b=0
#     c=a/b
#     print(f"The answer of a divide by b is {c}")
# except:
#     print(f"can't divide with zero. Provide a different number")







# # Catching Specific Exceptions
# try:
#     a=int(input("enter value of a: "))
#     b=int(input("enter value of b: "))
#     c=a/b
#     print(f"The answer of divide is {c}")
# except ValueError:
#     print("Entered value is wrong")
# except ZeroDivisionError:
#     print("Can't divide by zero")







# # Handle Multiple Exceptions With a Single Except Clause
# try:
#     a=int(input("enter any number "))
#     b=int(input("enter any number "))
#     c=a/b
#     print(f"The answer of a divide is {c}")
# except(ValueError,ZeroDivisionError):
#     print("please enter a valid value ")






# USING try WITH finally ==>> SYNTAX

# try:
#     block of code
#     this may throw an exception 
# finally:
#     block of code 
#     this will always be executed
#     after the try and any except block







# # try - except - finally
# try:
#     a=int(input("enter any number: "))
#     b=int(input("enter any number: "))
#     c=a/b
#     print(f"The divide of a by b is {c}")
# except ZeroDivisionError:
#     print("can't divide with zero")
# finally:
#     print("Inside a finally block")







# Using try with else clause ==syntax
# try:
    # block of code
# except Exception1:
    # block of code 
# else:
    # this code executes when exceptions not occured





# # use of else block with try
# try:
#     a=int(input('enter any number plz '))
#     b=int(input('enter any number plz '))
#     c=a/b
#     print(f"The divide is {c}")
# except ZeroDivisionError:
#     print("can't divide by zero")
# else:
#     print("we are in else block ")





# Raising an Exceptions ==>> syntax
# raise Exception_class,<value>



# # Example of Raising an Exception
# def simple_interest(amount,year,rate):
#     try:
#         if rate>100:
#             raise ValueError(rate)
#         interest=(amount*year*rate)/100
#         print(f"The simple interest is {interest}")
#         return interest
#     except ValueError:
#         print(f"Interes rate is out f range {rate}")
# print("case 1")
# simple_interest(800,6,8)

# print("case 2")
# simple_interest(800,8,200)








# # Exception Chaining 
# try:
#     a = int(input("enter value of a"))
#     b = int(input("enter value of b"))
#     c=a/b
#     print("The answer of a divide by b is {c}")

# except ZeroDivisionError as e:
#     raise ValueError("Division failed ")from e





# # Custom and User-defined Exceptions
# class Error(Exception):
#     """"Base class for other exceptions"""
#     pass

# class ValueTooSmallError(Error):
#     """"Raised when the input value is small """
#     pass

# class ValueTooLargeError(Error):
#     """"Raised when the input value is large"""
#     pass
# while(True):
#     try:
#         num=int(input("enter any value in 10 to 50 range "))
#         if num<10:
#             raise ValueTooSmallError
#         elif num>50:
#             raise ValueTooSmallError
#         break
#     except ValueTooSmallError:
#         print("Value is below range..try again")
#     except ValueTooLargeError:
#         print("value out of range...try again")
# print("Great! Value is in correct range")






# # Customizing Exception Classes
# class NegativeAgeError(Exception):
#     def __init__(self, age):
#         message="Age should not be in negative"
#         self.age=age
#         self.message=message

# age=int(input("Enter age: "))
# if age<0:
#     raise NegativeAgeError(age)





# # Exception Lifecycle Example NOTE This code will give error

# def sum_of_list(numbers):
#     return sum(numbers)

# def average(sum, n):
#     # ZeroDivisionError if list is empty
#     return sum / n

# def final_data(data):
#     for item in data:
#         print("Average:", average(sum_of_list(item), len(item)))

# list1 = [10, 20, 30, 40, 50]
# list2 = [100, 200, 300, 400, 500]
# # empty list
# list3 = []
# lists = [list1, list2, list3]
# final_data(lists)
