# fp=open('salex.txt','x')
# fp.close()



# fp=open('sales.txt','w')
# fp.write('This is first line ')
# fp.close()



# import os
# print(os.listdir())

# print(os.path.isfile('sales.txt'))


# with open(r"e:\Python And Django With Projects\hub it python\File handling\hello.txt","w") as fp:
#     fp.write("This is creating file with absolute path")
#     pass





# import os 
# path=r"e:\Python And Django With Projects\hub it python\File handling"
# file_name="revenue.txt"

# with open(os.path.join(path,file_name),'w') as fp:
#     fp.write("This is new line using absolute path")




# create a file if not exists

# import os 
# file_path=r"e:\Python And Django With Projects\hub it python\File handling\profit.txt"
# if os.path.exists(file_path):
#     print('file already exists')
# else:
#     with open(file_path,'w') as fp:
#         fp.write('This is second line')



# use file access mode x

# try:
#     file_path=r"e:\Python And Django With Projects\hub it python\File handling\profit2.txt"

#     with open(file_path,'x') as fp:
#         pass

# except:
#     print('file already exists')





# # create file with date and time

# from datetime import datetime
# x=datetime.now()

# file_name=x.strftime('%d-%m-%Y.txt')
# with open(file_name,'w')as fp:
#     print(f"The file created {file_name}")

# file_name2=x.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name2,'w')as fp:
#     print(f"The file created {file_name2}")

# file_name3=r"E:\Python And Django With Projects\hub it python\File handling\\" + x.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name3,'w')as fp:
#     print(f"The file created {file_name3}")







