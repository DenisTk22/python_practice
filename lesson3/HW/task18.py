# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите длину списка: '))
list_a = []
for i in range(n):
    list_a.append(input('Ведите число: '))
x = int(input('Какое число вас интересует? '))
dif_min = 1000
for i in range(n):
    dif = abs(x - int(list_a[i]))
    if dif_min >= dif:
        dif_min = dif
        nearest1 = int(list_a[i])
nearest2 = nearest1
if (x - nearest1) < 0:
    y = x - dif_min
    for i in range(n):
        print(list_a[i])
        if int(list_a[i]) == y:
            nearest2 = int(list_a[i])   
print('Ближайшее минимальное число = ', min(nearest1, nearest2))

 

