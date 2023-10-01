# Note-->> To create empty set do this 
# empty_set=set()
# print(type(empty_set))


# student_id={112,114,116,118,120}
# print(f"The all students id is {student_id}")



# Duplicate items in set
# numbers={73,1,3,4,11,83,4,2,1,}
# print(numbers)




# Updating and adding items in set
# In add-->> we can add only one item using add

# numbers={1,2,3,4}
# numbers.add(5)
# print(numbers)

# in updating we can update many more items
# numbers={1,2,3,4}
# b={5,6,7}
# b.update(numbers)
# print(b)


# removing elements from set

# languages={'swift','c','c++','java','python'}
# languages.discard('java')
# print(languages)


# Note Built in Functions with set
# a={1,2,3,4,5,6}
# b={14,23,12,7,8,10}
# print(sorted(b))
# print(len(a))
# print(max(b))
# print(min(a))
# print(sum(a))



# Python Set Operations
# Union of Two Sets
a={1,2,3,4,}
b={5,6,7,8,9}
# print("union of a and b is ", a | b)
# print('union of a and b is ', a.union(b))


# Intersection of two numbers 
# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9}
# print('intersection of a and b is ',a & b)
# print('intersection of a and b is ', a.intersection(b))


# only a  or  a-b is 
# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9}
# # print("only a is ",a -b)
# # print('only a is ', a.difference(b))

# print('only b is ',b-a)
# print("only b is ",b.difference(a))


# Only a and only b is 
# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9}
# print('only a and only b is ',a ^ b )
# print('only a and only b is ',a.symmetric_difference(b))



# check equality of sets
a={1,2,3,4}
b={4,2,3,1}
if a==b:
    print('a and b is equal')
else:
    print(' a and b are not equal')
    





