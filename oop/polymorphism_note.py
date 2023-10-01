# in built methods in poly
# students=['Emma','jessa','kelly']
# school='Holy Child'

# print('Reverse string')
# for i in reversed('PYnative '):
#     print(i,end=' ')

# print('\n Reverse list \n')
# for i in reversed(students):
#     print(i)



# user define methods 
# class Shape:
#     # Function with two default parameters 
#     def area(self,a,b=0):
#         if b>0:
#             print(f'Area of Rectangle is: {a*b}')
#         else:
#             print(f"Area of square is: {a**2}")

# square=Shape()
# square.area(5)

# rectangle=Shape()
# rectangle.area(5,3)







# over riding in polymorphism
# class Shopping:
#     def __init__(self,basket,buyer):
#         self.basket=list(basket)
#         self.buyer=buyer
#     def __len__(self):
#         print("Redefine length")
#         count=len(self.basket)
#         # count total items in a different way
#         # pair of shoes and shirt + pant
#         return count * 2
# obj_shopping=Shopping(['shoes','dress'],'Rahul')
# print(len(obj_shopping))







# def addition(a,b):
#     c=a+b
#     print(c)

# def addition(a,b,c):
#     d=a+b+c
#     print(d)

# # the below line shows an error 
# # addition (4,5)

# # This line will call the second product method
# addition(3,7,5)





# next Question 
# for i in range(5): print(i, end =' ')
# print()

# for i in range(5,10): print(i,end=' ')
# print()

# for i in range(2,12,2): print(i,end=' ')






# class Ferrari:
#     def fuel_type(self):
#         print('petrol')
#     def max_speed(self):
#         print("max speed 350")

# class BMW:
#     def fuel_type(self):
#         print('Diesel')
#     def max_speed(self):
#         print("max speed 240")

# # normal function 
# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()

# obj_ferrari=Ferrari()
# obj_bmw=BMW()

# car_details(obj_ferrari)
# car_details(obj_bmw)





# operator overloading

# # add 2 numbers 
# print(100+200)

# # concatenate two strings
# print('jessa','Roy')

# # merger two list
# print([10,20,30] + ['jessa', 'emma', 'kelly'])
