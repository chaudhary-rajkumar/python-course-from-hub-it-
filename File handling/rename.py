# # import os
# # os.rename('demo.txt','raj.txt')





# # Checking Whether file exist or not 

# # import os 

# # if os.path.isfile('kaliya.txt'):
# #     print("The file already exists ")

# # else:
# #     os.rename('raj.txt','kaliya.txt')






# # Rename Multiple Files in Python

# import os

# folder=f'E:\Python And Django With Projects\hub it python\File handling\\'
# count=1

# for file_name in os.listdir(folder):
#     source=folder+file_name
#     destination = folder + 'sales_' + str(count) + '.txt'

#     os.rename(source,destination)
#     count+=1

# print("All files are Renamed ")
# print("new files are ")
# res = os.listdir(folder)
# print(res)
