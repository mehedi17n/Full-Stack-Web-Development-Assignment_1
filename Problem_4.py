# Problem - 04
mylist = []
size = int(input('How many elements: '))
print('Enter elements numbers: ')

for i in range(size):
    n = int(input())
    mylist.append(n)

print(list(set(mylist)))