# Problem - 01
str = input("Enter a String: ")
if len(str) < 2:
    print("Empty String")
else:
    str1 = str[0:2]
    str2 = str[-2:]
    print(str1 + str2)