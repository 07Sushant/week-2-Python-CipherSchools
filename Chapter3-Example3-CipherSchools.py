# ask user name and count each letter
name = input("Enter your name: ")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]