# Problem - 03
mylist = []
size = int(input('How many elements: '))
print('Enter elements numbers: ')

for i in range(size):
    n = int(input())
    mylist.append(n)

max = 0

for n in mylist:
    if n > max:
        max = n

print('The largest number in list is', max)
