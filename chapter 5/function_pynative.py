# Creating a function without any parameters

# def message():
#     print("Welcome to PYnative")
# message()



# # Creating a function with parameters

# def cousre(name, c_name):
#     print(f"Hello {name} Welcome to Pynative")
#     print(f"your course name is {c_name}")
# cousre('Rajkumar','Python')




# # Creating function with parameters and return value 

# def calculator(a,b):
#     add=a+b
#     return add

# result=calculator(20,5)
# print(f"Addition is {result}")




# # Calling a Function
# def odd_even(n):
#     if n%2==0:
#         print('even number ')
#     else:
#         print('odd number')
# odd_even(12)





# Calling a function of a module
# from random import randint
# print(randint(1,20))





# # Docstring 
# def story():
#     '''This function returns the story of a given number. '''

# # accessing doc string
# print(story.__doc__)




# # docstring
# def any_fun(parameter1):
#     '''Description of function 
#     Arguments:
#     paramer1(int): Description of parameter1 
#     Returns:
#     int value '''
# print(any_fun.__doc__)






# # Retrun value from a function
# def is_even(list1):
#     even=[]
#     for n in list1:
#         even.append(n)
#     return even




# def arithmetic(a,b):
#     add=a+b
#     sub=a-b
#     multiply=a*b
#     division=a/b
#     return add, sub, multiply, division

# p,q,r,s=arithmetic(10,2)
# print(f'addition is {p}')
# print(f"subtraction is {q}")
# print(f"multiplication is {r}")
# print(f"division is {s}")






# global_lang='DataScience'

# def var_scope_test():
#     local_lang='Python'
#     print(local_lang)

# var_scope_test()
# print(global_lang)
# print(local_lang)
