# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7.

cubeslist = []
Sum7 = 0

# cube computing func
def cube(i):
    return i * i * i

# function to compute sum of digits in a number
def get_sum(i):
    digitSum = 0
    while i != 0:
        digitSum = digitSum + int(i % 10)
        i = int(i / 10)
    return digitSum
#adding odd number (in range 1-1000) into list
for i in range(1, 1000):
    if i % 2 != 0:
        cubeslist.append(cube(i))
print(cubeslist)
#getting the sum of a numbers (%7)
for i in cubeslist:
    if get_sum(i) % 7 == 0:
        Sum7 += get_sum(i)
print(Sum7)
