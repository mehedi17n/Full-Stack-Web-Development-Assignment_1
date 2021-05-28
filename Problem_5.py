# Problem - 05
def cmn(l1, l2):
    setl1 = set(l1)
    setl2 = set(l2)
    if len(setl1.intersection(setl2)) > 0:
        return (True)

print(cmn([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))