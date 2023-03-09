# #Задача 32: Определить индексы элементов списка,
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
n = int(input('Введите длину списка: '))
list1 = [random.randint(-10, 10) for _ in range(n)]
print(list1)
nmin = int(input('Введите нижнюю границу диапозона: '))
nmax = int(input('Введите верхнюю границу диапозона: '))
indexes = []
for i in range(n):
    if list1[i] <= nmax and list1[i] >= nmin:
        indexes.append(i)
        print(list1[i], end =' ')

print()
print(indexes)


#print([indexes.append(i) for i in range(n) if list1[i] <= nmax and list1[i] >= nmin])