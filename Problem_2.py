# Problem - 02
def rplce(str):
    snot = str.find('not')
    spoor = str.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str = str.replace(str[snot:(spoor + 4)], 'good')
        return str
    else:
        return str

print(rplce('The lyrics is not that poor!'))
print(rplce('The lyrics is poor!'))