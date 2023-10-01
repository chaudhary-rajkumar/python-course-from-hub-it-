# fp=open(r"E:\Python And Django With Projects\hub it python\File handling\profit.txt",'r')

# print(fp.read())
# fp.close()




# opening file with relative path

# try:
#     fp=open("profit.txt", "r")
#     print(fp.read())
#     fp.close()

# except FileNotFoundError:
#     print("Please check the file path")





# fp=open('sample2.txt','w')
# fp.write("This is new line ")

# fp=open('sample2.txt','r')
# print(fp.read())
# fp.close()




# fp=open('sample2.txt','a')
# fp.write('Added this line by opening file in a append mode ')

# fp=open('sample2.txt','r')
# print(fp.read())
# fp.close()






# # Opening file using "with" statement
# with open('sample1.txt','r', encoding='utf-8') as infile, open('sample2.txt','w') as outfile:
#     for line in infile:
#         outfile.write(line)

# fp=open('sample2.txt','r')
# print(fp.read())
# fp.close()



# # Creating a new file 
# try:
#     with open('sample3.txt','x') as fp:
#         fp.write("Hello World! I am a new file ")
#     fp=open('sample3.txt','r')
#     print(fp.read())

# except FileExistsError:
#     print("The file already exists ")

    



# opening a file for multiple operations 

# with open('sample3.txt','r+') as fp:
#     print(fp.read())

#     fp.write("\n Adding this new content")
#     fp.close()



