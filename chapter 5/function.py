# def detail(a,b,c=20):
#     # print("helllo world")
#     # return("helllo world")
#     return(a+b+c)
# detail(10,12)


# print(detail(10,15,30))


# num=int(input("enter a num"))
# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")

# even_odd(num)



# local variable and global variable
# c=20
# def sum():
#     print(c)
#     global a
#     a=10
#     b=20
#     print(a+b)
#     print(a)
# sum()
# print(a)




# args and kwargs

## in def function(normal argument, default argument, args and kwargs)
# def detail(a,b,*args,c=10, **kwargs):
#     print(a,b)
#     print(type(args))
#     print((args))
#     print((kwargs))

# detail(1,2,4,5,8,6,8,address="ABC",fruits="apple",)



# Args
# def holi(*args,a=10):
#     print(a)
#     print(args)
#     print(type(args))
#     print(sum(args))

# holi(2,33,3,56,5,4,)

# kwargs
# def kalu(x,y=10,**kwargs):
#     print(x)
#     print(y)
#     print(kwargs)
#     a=kwargs.values()
#     str1=" "
#     print(str1.join(a))
#     # print(a)
# kalu(12,a='raj',b='hi',c='hello',d='how')



# Q.N. sum
# sum=lambda a,b : a*b
# print(sum(2,5))



# Q.N. odd even
# even_odd=lambda n=int(input("enter any num")) :f"{n } is even"  if n%2==0  else f"{n} is odd"
# print(even_odd(1))




# lamda function in list comprehension
# lst=[1,2,3,4,5,6,7,]
# lst2=list(filter(lambda x: x%2==0,lst))
# print(lst2)





# filter function in  list comprehension 
# lst=[1,2,3,4,5,6,7,]
# def even_odd (x):
#         if x%2==0:
#             return x

# lst2=list(filter(even_odd,lst))
# print(lst2)




# map function using lamda 
# lst=[2,3,4,5,6,7]
# squar=list(map(lambda x: x*x,lst))
# print(squar)



# map function in list comprehension
# lst=[1,2,3,4,8,43,5]
# def squa(x):
#     x=x*x
#     return x
# y=list(map(squa,lst))
# print(y)




# def sum():
#     a=10
#     b=12
#     c=a+b
#     print(c)
# sum()



# def sum(a,b):
#     c=a+b
#     print(c)
# sum(12,43)




def oe():
    a=int(input('enter any number'))
    if a%2==0:
        print('even number')
    else:
        print('odd number')


oe()
