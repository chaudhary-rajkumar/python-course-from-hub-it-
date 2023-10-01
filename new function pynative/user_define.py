# def course_func(name,course_name):
#     print(f"Hello {name} Welcome to pynative")
#     print(f"your course name is {course_name}")
# course_func('Raj','Python')





# def calculator(a,b):
#     add=a+b
#     return add
# res=calculator(20,5)
# print(f"Addition is : {res}")



# # calling a function
# def even_odd(n):
#     if n%2==0:
#         print('even number')
#     else:
#         print('odd number ')
# even_odd(11)




# # calling a function of a module
# from random import randint
# print(randint(1,10))




# Docstrings
# Answer=> In Python, the documentation string is also called a docstring. It is a descriptive text (like a comment) written by a programmer to let others know what block of code does.
# We write docstring in source code and define it immediately after module, class, function, or method definition.
# It is being declared using triple single quotes (''' ''') or triple-double quote(""" """).





# single line docstring
# def factorial(x):
#     """This function returns the factorial of a given number."""
#     return x
# print(factorial.__doc__)

# print(help(factorial))





# Multi line docstring
# def any_func(parameter1):
#     """
#     Description of function
#     Arguments:
#     Parameter1(int):Description of parameter1
#     Retruns:
#     int value
#     """
# print(any_func.__doc__)





# Return value from a function
def is_even(list1):
    even_num=[]
    for n in list1:
        if n%2==0:
            even_num.append(n)
    return even_num
even_num=is_even([1,2,3,4,5,6,7,8,9,10])
print(f"Even numbers are: {even_num}")
