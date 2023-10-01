# # Read a text file 
# try:
#     fp = open('hello.txt','r')
#     print(fp.read())
#     fp.close()
# except FileExistsError:
#     print('Please check the path')






# # Reading a File Using the with Statement

# with open('sales.txt','r') as fp:
#     print(fp.read())
#     fp.close()





# # use of readline(n)

# with open('hello.txt', 'r') as fp:
#     print(fp.readline())





# # Reading First N lines From a File Using readline()

# with open('hello.txt','r') as fp:
#     # reading 3 lines 
#     for i in range(3):
#         print(fp.readline().strip())





# # Reading Entire File Using readline()
# with open('sales.txt','r') as fp:
#     line=fp.readline()
#     while line !='':
#         print(line, end='')
#         line=fp.readline()




# Reading First and the last line using readline()

# with open ('hello.txt','r') as file:
#     first_line=file.readline()
#     print(first_line)
#     for last_line in file:
#         pass 
#     print(last_line)





# # Reading file into list 

# with open('sales.txt','r') as fp:
#     lines=fp.readlines()
#     print(lines)





# # Reading First n lines from a file 

# n=2
# with open('hello.txt','r') as fp:
#      head=[next(fp) for x in range(n)]
# print(head)





# # Reading last 2 lines from the file 

# n=2
# with open('hello.txt','r') as fp:
#     lines=fp.readlines()[n:]
# print(lines)






# # Reading N bytes from the file 

# try:
#     fp=open('hello.txt','r')
#     print(fp.read(30))
#     fp.close()
# except FileNotFoundError:
#     print('Please check the path')






# # Reading and Writing to the same file

# with open('demo.txt','r+') as fp:
#     print(fp.read())

#     fp.write("\n Adding Sixth line in the file ")
#     print(fp.read())






# # Reading File in Reverse Order

# with open('hello.txt','r') as fp:

#     lines=fp.readlines()
#     for i in reversed(lines):
#         print(i)
