# # seek :- seek is a function sets the position of a file pointer and the tell() function returns the current position of a file pointer.


# # with open('sample1.txt','r') as fp:
# #     fp.seek(6)
# #     print(fp.read())





# # Seek the Beginning of the file 
# with open('demo.txt','w+') as fp:
#     fp.write('\nMy first line \n ')
#     fp.write('my second line ')
#     # move pointer to the beginning 
#     fp.seek(0)
#     print(fp.read())






# # Seeking The End of File 

# with open('demo2.txt','r+') as fp:
#     fp.seek(0,2)
#     fp.write('\nThis content is added to the end of the file ')
#     fp.seek(0)
#     print(fp.read())





# # Seek From The Current Position

# with open ('demo2.txt','rb')as fp:
#     fp.seek(3)
#     print(fp.read(5).decode('utf-8'))
#     fp.seek(10,1)
#     print(fp.read(6).decode('utf-8'))
    




# # Seek Backward With Negative Offset

# with open('demo2.txt','rb') as fp:
#     fp.seek(-40,2)
#     print(fp.read(11).decode('utf-8'))





# # To Seek Backwards From Current Position

# with open('demo2.txt','rb') as fp:
#     print(fp.read(8).decode('utf-8'))

#     fp.seek(-5,1)
#     print(fp.read(10).decode('utf-8'))








# Tell() Function to get file handle position

# open file for reading and writing  r+
with open(r'demo2.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # getting the file handle position
    print('file handle at:', fp.tell())

    # writing new content
    fp.write("\nDemonstrating tell")

    # getting the file handle position
    print('file handle at:', fp.tell())

    # move to the beginning
    fp.seek(0)
    # getting the file handle position
    print('file handle at:', fp.tell())

    # read entire file
    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')

    # getting the file handle position
    print('file handle at:', fp.tell())
