cubeslist = []
Sum7 = 0

def cube(i):
    return i * i * i


for i in range(1, 1000):
    if i % 2 != 0:
        cubeslist.append(cube(i))
print(cubeslist)

for i in cubeslist:
    if i % 7 == 0:
        Sum7 +=  i
print(Sum7)
# print (cubeslist)
