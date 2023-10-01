# Q.N. sum
# sum=lambda a,b : a*b
# print(sum(2,5))



# odd_even=lambda a=input('enter the value of a'): "even number" if a%2==0 else " odd number "
# print(odd_even(3))











# Q.N. odd even
# even_odd=lambda n=int(input("enter any num")) :f"{n } is even"  if n%2==0  else f"{n} is odd"
# print(even_odd(1))


# list question using lamda 
# lst_lab1 = lambda lst=['d','ef','hi',12] , blst=[], : print("hello world")


# list comprehension using filter function 
# lst=[1,2,3,4,5,6,7,]
# def even_odd (x):
#         if x%2==0:
#             return x

# lst2=list(filter(even_odd,lst))
# print(lst2)


# lamda function in list comprehension
lst=[1,2,3,4,5,6,7,]
lst2=list(filter(lambda x: x%2==0,lst))
print(lst2)