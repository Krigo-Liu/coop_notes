
def haha(random):
    if random == 0:
        return 0
    if random == 0.5:
        return 0
    return False # two different outcomes with 0 （False） and other numbers（True）


print(haha(0))
print(haha(0.5))
print(haha(6))
print("----------")

alist = []
if haha(0):
    alist.append("biu")
print(alist)

if haha(6):
    alist.append("biu")
print(alist)

print([0]*22)