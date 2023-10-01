# Q.N. 1
# a=input("enter any string \n")
# b=int(input("enter any index number"))
#  if len(a)==0:
#     print("String is empty ")
# elif b>=len(a):
#     print("index is out of range ")
# else:
#     print(a[b])



# Q.N. 2
# string = input("Enter a string: ")

# if len(string) == 0:
#     print(string)
# else:
#     reversed_string = ""
#     for i in range(len(string)-1, -1, -1):
#         reversed_string += string[i]
#     print(reversed_string)





# Q.N. 3
# a=input("Enter any string please \n")
# b=""
# for i in range(1,len(a),2):
#     b=b+a[i]
# print(b)

# ---->> Another way to solve this question
# a=input("enter any string \n ")
# print(a[1::2])





# Q.N. 4
# a=input("Enter your name").lower()
# b=int(input("Enter your age"))

# if a[0]=="a" and b>=18:
#     print("you can vote ")
# else:
#     print("you can not vote")



# # Q.N.5
# i=0
# sum=0
# while i<11:
#     sum=sum+i
#     i=i+1
# print(f"The total sum of first 10 natural number is {sum}")



# # Q. N. 6 
# r=input("Enter any string please \n").lower() # rajkumar

# a="" # r
# for i in range(0,len(r)):
    
#     if r[i] not in a:
#         a=a+r[i]
#         print(f"{r[i]} : {r.count(r[i])}")



# Q.N. 7 
# a=input("enter any string ")
# b=input("which string you want to change ")
# c=input("with which string you want to change ")

# print(a.replace(f"{b}",f"{c}"))




 # Q.N. 8
# a=int(input("enter any number please"))

# if a>0: 
#     print(f"{a} is positive")
# elif a<0:
#     print(f"{a} is negetive")
# else:
#     print(f"{a} is zer0")



# Q.N. 9
# a=input("enter any number please \n")
# b=input("enter any number please \n")
# c=input("enter any number please \n")
# if a==b==c:
#     print(f"{a} {b} {c} are equal")
# else:
#     print(f"{a} {b} {c} are not equal")



# Q.N. 10
# import random
# print("welcome to my Legendary game ".title())
# possible_action=["paper","scissor","rock"]
# computer_action=random.choice(possible_action)
# user_action=input("Enter any choice (paper scissor or rock)  ").lower()

# print(f"your choice is {user_action}")
# print(f"And computer choice is {computer_action}")

# if user_action==computer_action:
#     print(f"both chossed {user_action} and {computer_action} so match tie")
# elif user_action=='paper':
#     if computer_action=='scissor':
#         print("scissor cut paper you lost")
#     else:
#         print("paper cover rock you win ")
# elif user_action=='scissor':
#     if computer_action=="rock":
#         print("rock smash scissor you lost")
#     else:
#         print("scissor cut paper you win ")
# elif user_action=="rock":
#     if computer_action=='paper':
#         print("paper covers the rock you lost")
#     else:
#         print("rock smash the scissor you win")



# Q.N. 11
# a=input("enter any number please \n")
# print(a[::-1])



# Q.N. 12
1

# num=int(input("enter any number please \n"))     #7
# for i in range (2,num):
#     if num % i == 0:
#         print("not prime ")
#         break
# else:
#         print("prime")





# Q.N. 13
# a=input("enter any string \n")
# b=""
# for i in range(len(a)-1, 0):
#     b=b+a[i]
# print(b)



# Q.N. 14
# for i in range(1,6):
#     print("*" * i)






# Q.N. 15
# import random
# r_number=random.randint(1,100)

# while True:
#     user_number=int(input("enter any number please \n"))
#     if user_number==r_number:
#         print("**** you **** win ****")
#         break
#     elif user_number>r_number:
#         print("Very high number")
#     else:
#         print("Very low number")






# Q.N. 16
# a=int(input("enter any number "))
# b=int(input("enter any number "))
# print("Welcome to calculator".center(40, "*"))
# ch=int(input(''' choose any operation 1 to 4
# 1. Addtion
# 2. Subtraction
# 3. Multiplication
# 4. Division \n'''))

# if ch==1:
#     print(f"The sum of a and b is {a+b}")
# if ch==2:
#     print(f"The subtraction of a and b is {a-b}")
# if ch==3:
#     print(f"The multiply of a and b is {a*b}")
# if ch==4:
#     print(f"The division of a and b is {a/b}")

# print("Thanks for using calculator".title().center(40,"*"))


