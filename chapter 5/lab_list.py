# Q.N. 1
# lst=['d','ef','ij','87']
# blst=[]
# a='abc'
# for i in lst:
#     blst.append(i+a)

# print(blst)









# Q.N. 2
# lst=['hello','this','is','python']
# c=''
# for i in lst:
#     c=c+i

# print(c)



# Q.N.3
# a=['hello','how','are','you']
# if len(a)==0:
#     print('empty list')
# else:
#     print('not empty list')




# # Q.N. 4
# a=['hello ','this ','is ','python']
# b=''
# c=[]
# for i in a:
#     b=b+i
# print(b)
# c.append(b)
# print(c)







# Q.N. 5

# a=['i ', 'am ' , 'learning ', 'python ']
# b=''
# c=[]
# for i in a:
#     b=b+i
# c.append(b)
# print(c)







# q.n.6
# eg=["hello",'this', "this" , "is ",'python', "python"] 
# a=[]
# for i in eg:
#     if i not in  a: 
#         a.append(i)
# print(a)





# Q.N.6

# lst=['hi','i','love','python','and','python']
# lst1=[]
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
#     else:
#         lst.remove(i)
# print(lst)






# Q.N. 7        --->>> if list contains strings
# count=0
# lst=['hello','how','are','you','my','dear','friend','i',]
# for i in lst:
#     if len(i) > 3:
#         count=count+1
# print(count)



# Q.N.7
# lst=[0,1,2,3,4,5,9,34,73,829,0]
# count=0
# for i in lst:
#     if i>3:
#         count=count+1
# print(count)



# Q.N. 8
# lst_a=[1,2,3,4,5]
# lst_b=[1,3,5,]
# lst3=[]
# for i in lst_a:
#     if i not in lst_b:
#         lst3.append(i)
# print(lst3)




# # Q.N. 9
# list_a=[3,5,9,12,839,23,23,8383]
# list_a.sort()
# print(list_a)
# print(f"the second highest value is \n {list_a[-2]}")



# # Q.N.10
# lya=[5,7,['hello','rajkumar'],2,['butwal']]
# lyb=[]
# for i in lya:
#     if type(i) is list:
#         for a in i:
#             lyb.append(a)
#     else:
#         lyb.append(i)
# print(lyb)






# taking input in list
# a=input('enter numbers ').split()

# print(a)
# print(type(a))



a=input("enter any value")
b=input("enter any value")
c=input("enter any value")
d=input("enter any value")
e=input("enter any value")
f=input("enter any value")

m=[a,b,c,d,e,f]
print(m)
