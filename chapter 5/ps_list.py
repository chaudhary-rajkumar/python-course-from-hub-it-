# # Question Number 1
# lst=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# # for i in range(1,len(lst)+1):   -->> this 
# for i in lst:                     -->>  and this are same
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print([even,odd])


# # Q.N.2
# A=[2,1,5,7,8,6]
# B=[3,4,5,9,6,2]
# c=[]

# for i in A:
#     if i in B:
#         c.append(i)
# print(c)


# Q.N. 3
# A=['hi', 'ho',[2,4,5,6], 'hoho', 'sorry','no']
# B=[]
# for i in range(len(A)):
#     B.append(A.pop())
# print(B)


# # Q.N.4
# a=['abc' , 'def' , 'ghi']

# lst=[]
# for i in a:
#     lst.append(i[::-1])
# print(lst)



# Q.N. 5

lst=['apple','orange','avacode','banana']

alst=[]
blst=[]
for i in lst:
    if i.startswith('a' or 'A'):
        alst.append(i)
    else:
        blst.append(i)

print(alst)
print(blst)





