cubeslist = []


def cube(i):
    return i * i * i


for i in range(1, 1000):
    if i % 2 != 0:
        cubeslist.append(cube(i))
print (cubeslist)

Sum = sum(cubeslist)
print (Sum)
# print (cubeslist)
