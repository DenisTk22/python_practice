# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

import random
n = int(input('Введите количество оценок: '))
array = [random.randint(1,5) for i in range(n)] #randint берет от 1 до 5
print(array)
nmin = min(array)
nmax = max(array)
a = [nmin if i == nmax else i for i in array]# nmin if i == nmax - если i = nmax, то заменить на nmin, иначе i, перебор по элементам i в массиве array
print(a)

