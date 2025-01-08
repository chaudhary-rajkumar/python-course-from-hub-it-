name=input("Enter your name: ").lower()
b=""
for i in range(0, len(name)):
    if name[i] not in b:
        b=b+name[i]
        print(f"{name[i]} : {name.count(name[i])}")