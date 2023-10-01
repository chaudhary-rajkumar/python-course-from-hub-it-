name=input('enter any string \n')   #raj
rev=""
for i in range(len(name)-1 ,-1,-1):
    rev=rev+name[i]
print(rev)