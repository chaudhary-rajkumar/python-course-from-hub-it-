# # Write to a text file in a python 

# text='This is new content'
# fp=open('demo1.txt','w')
# fp.write(text)
# fp.close()


# fp=open('demo1.txt','r')
# print(fp.read())
# fp.close()






# # Writing to an existing file 

# fp=open('demo.txt','r')
# print(fp.read())
# fp.close()

# fp=open('demo.txt','w')
# fp.write("This is overwriteen content")
# fp.close()

# fp=open('demo.txt','r')
# print('opening file again')
# print(fp.read())
# fp.close()






# # Write a list of lines to a file 

# personal_data=['Name:Emma', '\n Address: Rohini-3, Rupandehi','\n City = Bhairahwa ']
# fp=open('call.txt','w')
# fp.writelines(personal_data)
# fp.close()

# fp=open('call.txt','r')
# print(fp.read())
# fp.close()






# # With Statement to write a file 

# name='Written using a context manager'
# with open('sample2.txt','w') as fp:
#     fp.write(name)

# with open('sample2.txt','r') as fp:
#     print(fp.read())





# # Appending New Content to an existing file 

# name='\nRajkumar Chaudhary'
# address=[ '\nAddress : Rohini-3 , Rupandehi ', '\nCite : Bhairahwa','\nCountry : Nepal ' ]
# with open('sales2.txt','a') as fp:
#     fp.write(name)
#     fp.writelines(address)

# with open('sales2.txt','r') as fp:
#     print(fp.read())





# Append and Read on the Same file 

# name='\nRajkumar Chaudhary'
# address=[ '\nAddress : Rohini-3 , Rupandehi ', '\nCite : Bhairahwa','\nCountry : Nepal ' ]
# with open('sample1.txt','a+') as fp:
#     fp.write(name)
#     fp.writelines(address)
#     fp.seek(0)
#     print(fp.read())






# with open('call.txt','w+') as fp:
#     fp.write('kelly is a character of a game ')
#     fp.seek(0)
#     print(fp.read())
