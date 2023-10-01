# a=input("Enter any string value \n")
# b=input("Enter any string value \n")
# c=input("Enter any string value \n")

# if len(a)==0 or len(b)==0 or len(c)==0:
#     print("Your string is empty")
# else:
#     first_char=a[0:2]
#     second_char=b[len(b)//2:(len(b)//2)+2]
#     third_char=c[len(c)-2:]
#     print(first_char+second_char+third_char)



# Second Question 

a=input("enter any string \n")
if len(a)<=5:
    print("Your string is very small ")
else:
    first_char=a[0:3]
    second_char=a[len(a)-3:]
    
    print(first_char+second_char)


# THIRD QUESTION
# a=int(input("enter any number"))
# b=int(input("enter any number"))

# if a==b:
#     print(" a and b is equal")
# elif a>b:
#     print("a is greatest than b")
# else:
#     print("b is greates than a")




# FOURTH QUESTION

# a=int(input("Enter any string \n "))
# b=int(input("Enter any string \n "))
# c=int(input("Enter any string \n "))
# if a==b==c:
#     print("All values are equal")
# elif a==b or a==c or b==c:
#     print("Two numbers are equal")
# elif a>b and a>c:
#     print(f"The greatest value is {a}")
# elif b>a and b>c:
#     print(f"The greatest value is {b}")
# # elif c>a and c>b:
# else:
#     print(f"The greates value is {c}")



# FIFTH QUESTION
# name=input("Enter any number value ")
# a=0
# sum=0
# while a<len(name):
#     sum=sum+int(name[a])
#     a=a+1
# print(sum)


# Sixth Question
# check=""
# a=0   
# name=input("enter any string").lower()
# while a<len(name):
#     if name[a] not in check:
#         check=check+name[a]
#         print(f"{name[a]}:{name.count(name[a])}")
#     a=a+1



